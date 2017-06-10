from django.shortcuts import render,HttpResponseRedirect,redirect,Http404, HttpResponse, render_to_response
from django.contrib.auth import authenticate, login, logout
from KYusers.emailBackend import LoginUsingEmailAsUsernameBackend
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from django.contrib.messages import get_messages

from django.contrib.auth.decorators import login_required
from KYusers.models import *
from events.models import *
from KYusers.forms import *
from events.models import *

from scripts.casheet import CASheetUpdate
from scripts.kysheet import KYSheetUpdate
from django.core.mail import EmailMultiAlternatives

@login_required(login_url = "/form")
def eventPage(request):
    template_name = 'events.html'

    context = {
    'parentEvents' : ParentEvent.objects.all(),
    }
    return render(request, template_name, context)


def regCheck(request, kyprofile, event):
    print 'checking ', kyprofile
    alreadyReg = False
    try:
        Team.objects.get(event=event, teamLeader=kyprofile)
        alreadyReg = True
    except:# not a team leader
        try:
            Team.objects.get(event=event, members=kyprofile)
            alreadyReg = True
        except:#not reg as team member too
            pass

    if alreadyReg:
        print 'alreadyReg'
        try:
            messages.info(request, '%s already registered for event : %s.' %(kyprofile.kyId, event.eventName), fail_silently=True)
        except:
            pass
    return alreadyReg

@login_required(login_url = "/form")
def eventRegistration(request, eventName):
    event = Event.objects.get(eventName=eventName)
    template_name = 'eventRegister.html'
    context = {
        'event':event,
    }
    kyprofile = request.user.kyprofile
    regCheck(request, kyprofile, event)

    if request.method == "POST":

        post = request.POST
        print post
        teamName = post['teamName']
        leaderId = post['leader']
        memberIds = post.getlist("fields[]")
        try:
            teamLeader = KYProfile.objects.get(kyId = leaderId)
            regCheck(request, teamLeader, event)
        except Exception as e:
            messages.error(request, 'Team Leader\'s KY Id: %s is Invalid. (letters are case sensetive!)' %leaderId, fail_silently=True)
            return render(request, template_name, context)
        team = Team(teamName=teamName, event=event, teamLeader=teamLeader)
        membersList = []
        for Id in memberIds:
            if Id is not '':
                try:
                    kyprofile = KYProfile.objects.get(kyId=Id)
                    regCheck(request, kyprofile, event)
                    membersList.append(kyprofile)
                except Exception as e:
                    # print e
                    messages.error(request, 'KY Id: %s is Invalid. (letters are case sensetive!)', fail_silently=True)
                    return render(request, template_name, context)

        msg = messages.get_messages(request)
        if msg:
            print msg
            return render(request, template_name,context)

        team.save()
        team.members.add(*membersList)
        team.save()

        messages.success(request, 'Registration for %s successfull!' %(eventName), fail_silently=True)
        return render(request, template_name, context)
    else:
        return render(request,template_name, context)

def conCheck(request, kyprofile):
    template_name = 'eventRegister.html'
    print 'checking ', kyprofile
    alreadyReg = False
    try:
        Contingent.objects.get(contingentLeader=kyprofile)
        alreadyReg = True
    except:# not a team leader
        try:
            Team.objects.get(members=kyprofile)
            alreadyReg = True
        except:#not reg as team member too
            pass

    if alreadyReg:
        print 'alreadyReg'
        messages.info(request, '%s already registered for Contingent.' %(kyprofile.kyId), fail_silently=True)
        return redirect('/contingent')
    else:
        pass

@login_required(login_url = "/form")
def contingentRegistration(request):
    template_name = 'contingent.html'
    if request.method == "POST":
        post = request.POST
        print post
        leaderId = post['leader']
        memberIds = post.getlist("fields[]")

        try:
            teamLeader = KYProfile.objects.get(kyId = leaderId)
            conCheck(request, teamLeader)

        except Exception as e:
            print e
            messages.info(request, 'Team Leader\'s KY Id: %s is Invalid. (letters are case sensetive!)' %leaderId, fail_silently=True)
            return redirect('/contingent')
        contingent = Contingent(contingentLeader=teamLeader)
        membersList = []
        for Id in memberIds:
            if Id is not '':
                try:
                    kyprofile = KYProfile.objects.get(kyId=Id)
                    conCheck(request, kyprofile)

                    membersList.append(kyprofile)
                except Exception as e:
                    print e
                    messages.info(request, 'KY Id: %s is Invalid. (letters are case sensetive!)' %Id, fail_silently=True)
                    return redirect('/contingent')

        msg = messages.get_messages(request)
        if msg:
            print msg
            return redirect('/contingent')

        contingent.save()
        contingent.members.add(*membersList)
        contingent.save()

        messages.success(request, 'Contingent Registration is successfull!', fail_silently=True)
        return redirect('/contingent')
    else:
        return render(request, template_name, {})

def individualReg(request):
    if request.method == "POST":
        response_data = {}
        kyId = request.POST.get('kyId')
        eventId = request.POST.get('eventId')
        try:
            kyprofile = KYProfile.objects.get(kyId=kyId)
            print kyprofile
            event = Event.objects.get(eventId=eventId)
            print event
        except Exception as e:
            response_data['error'] = str(e)
            return HttpResponse(
                json.dumps(response_data),
                content_type = "application/json"
                )
        request=None
        if not regCheck(request,kyprofile, event):
            Team.objects.create(teamLeader=kyprofile, event = event)
            response_data['status'] = 'registered'
            return HttpResponse(
                json.dumps(response_data),
                content_type = "application/json"
                )
        else:
            return HttpResponse('already registered!')
    else:
        return HttpResponse('not allowed')

def regCheckAjax(request):
    if request.method == "POST":
        response_data = {}
        kyId = request.POST.get('kyId')
        eventId = request.POST.get('eventId')
        kyprofile = KYProfile.objects.get(kyId=kyId)
        event = Event.objects.get(eventId=eventId)
        request = None
        if regCheck(request,kyprofile, event):
            response_data['status'] = 'registered'
        else:
            response_data['status'] = 'not_registered'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        return HttpResponse('not allowed')

@login_required(login_url = "/form")
def dashboard(request):
    template_name = 'dashboard.html'
    kyprofile = request.user.kyprofile
    context = {
        'indTeams': Team.objects.filter(teamLeader=kyprofile, members=None).all(),
        'memTeams' : Team.objects.filter(members=kyprofile).all(),
        'leadTeams':Team.objects.filter(teamLeader=kyprofile).all()
    }
    print context['memTeams']
    return render(request, template_name, context)

def deregister(request):
    if request.method == "POST":
        print request.POST
        response_data = {}
        teamId = request.POST['teamId']
        kyId = request.POST['kyId']
        team = Team.objects.get(teamId=teamId)
        kyprofile = KYProfile.objects.get(kyId=kyId)
        print team, kyprofile
        if team.members.all().count()==0: # ind reg
            team.delete()
            response_data['status'] = 'deregistered'

        else:
            team.members.remove(kyprofile)
            team.save()
            response_data['status'] = 'deregistered'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        return HttpResponse('not allowed')
