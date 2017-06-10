from django.shortcuts import render,HttpResponseRedirect,redirect,Http404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from KYusers.emailBackend import LoginUsingEmailAsUsernameBackend
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from KYusers.models import *
from KYusers.forms import *
from events.models import *

from scripts.casheet import CASheetUpdate
from scripts.kysheet import KYSheetUpdate
from django.core.mail import EmailMultiAlternatives

server = 'http://kashiyatra.herokuapp.com/'

def send_email(subject, body, email):

    mail = EmailMultiAlternatives(
      subject = subject,
      body = body,
      from_email = "Kashiyatra <kashiyatra@iitbhu.ac.in>",
      to = [email],
      headers = {"Reply-To":"kashiyatra@iitbhu.ac.in"},
    )

    mail.send()
    return True

def context_call(request):

    context = {
        'user': request.user,
            }
    return context

def IndexView(request):
    template_name = 'index.html'
    return render(request,template_name,{})

def RegisterView(request,template_name,context):
    post = request.POST
    context = {
        'all_colleges':College.objects.all(),
    }
    mobileNumber = post.get('mobileNumber')
    email = post.get('email')
    if len(post.get('mobileNumber')) !=10 or '@' not in email or '.' not in email:
        messages.warning(request,'Please fill the form Correctly!', fail_silently=True)
        return redirect('/form')

    user,created = User.objects.get_or_create(username=email[:30],email=email)
    if created:
        # print 'USER CREATED'
        user.first_name = post.get('name')
        password = post.get('password')
        user.set_password(password)
        user.is_active = False #to be True after email confirmation

        user.save()
        sex = post.get('sex')
        year = post.get('year')
        ref = post.get('referralCode')

        college, created = College.objects.get_or_create(collegeName=post.get('college'))
        college.regCount += 1
        college.save()

        KYProfile(user=user,sex=sex,year=year,mobileNumber=mobileNumber,college=college, referralCode=ref).save()
        # new_user = authenticate(username=email, password=password)
        # login(request, new_user)
        kyprofile = KYProfile.objects.get(user=user)
        KYSheetUpdate(kyprofile)
        # messages.success(request,'KY registration successful, your KY id is'+kyprofile.kyId ,fail_silently=True)
        try:
            ca = CAProfile.objects.get(caId=ref)
            ca.regNum = ca.regNum + 1
            ca.regs.add(kyprofile)
            ca.save()
        except Exception as e:
            print e
            pass

        confirmationKey = 'Kashiyatra2017' + email + "asdfj2314sdlf"
        confirmationKey = str(hash(confirmationKey))
        try:
            key = Key.objects.get(kyprofile = kyprofile)
            key.confirmationKey = confirmationKey
            key.save()
        except:
            key = Key(kyprofile = kyprofile, confirmationKey = confirmationKey)
            key.save()

        subject = 'Email Confirmation for KY\'17'
        body = "Please Cick on the following link to confirm your Email and complete your registration for Kashiyatra 2017!.\n\n"
        body += server + "confirmEmail/" + confirmationKey

        if send_email(subject, body, email):
            messages.success(request, 'Confirmation mail sent!, Please check your mail.', fail_silently=True)
            return redirect('/form')
        else:
            message.warning(request, 'Email Confirmation link can\'n be sent please try to register again.', fail_silently=True)
            return render(request,template_name,context)

    else:#allready a user
        messages.warning(request,'email allready registered!',fail_silently=True)
        return render(request,template_name,context)


@csrf_exempt
def confirmEmail(request,confirmationKey):
    if request.method == 'GET':
        try:
            key = Key.objects.get(confirmationKey = int(confirmationKey))
            return render(request,"emailConfirm.html")
        except:
            messages.warning(request,'Invalid Url!')
            return redirect('/form')

    elif request.method == "POST":
        post = request.POST
        try:
            key = Key.objects.get(confirmationKey=confirmationKey)
            kyprofile = key.kyprofile
            kyprofile.user.is_active = True
            kyprofile.user.save()
            messages.success(request, "Email Confirmed!", fail_silently=True)
            return redirect('/form')
            # try:
            #     user = PasswordlessAuthBackend().authenticate(username=caprofile.user.email)
            #     user.backend = 'ca.backend.PasswordlessAuthBackend'
            #     login(request,user)
            #     return render(request,'ca/thanks.html',{})
            # except Exception as e:
            #     return HttpResponse(e)
        except:
            raise Http404('Not allowed')


def LoginView(request,template_name,context):
    post = request.POST
    email = post.get('email')
    password = post.get('password')
    form = LoginForm(request.POST)
    print form.is_valid()
    user = LoginUsingEmailAsUsernameBackend().authenticate(email=email, password=password)
    print user
    if user is not None:
        user.backend = 'KYusers.emailBackend.LoginUsingEmailAsUsernameBackend'
        if user.is_active:
            login(request, user)
            return redirect('/profile')
        else:
            messages.warning(request, "Please Confirm your email before logging in, for email confirmation check your email.", fail_silently=True)
            return redirect('/login')
    else:
        messages.error(request,'Invalid Credentials',fail_silently=True)
        return render(request,template_name,context)

def FormView(request):
    if request.user.is_authenticated():
        return redirect('/profile')

    context = {
    "regform" : RegisterForm(),
    "logform" : LoginForm(),
    "all_colleges" : College.objects.all(),
    }
    template_name = 'form.html'
    if request.method == "POST":
        if "register" in request.POST:
            return RegisterView(request,template_name,context)
        elif "login" in request.POST:
            return LoginView(request,template_name,context)
    else:
        return render(request,template_name,context)

@login_required(login_url='/form')
def CARegisterView(request):
    context = {
    'form' : CARegisterForm(),
    }
    template_name = 'ca-register.html'
    if request.method == 'POST':
        post = request.POST
        form = CARegisterForm(request.POST)
        if form.is_valid():
            ca = form.save(commit=False)
            ca.kyprofile = request.user.kyprofile
            ca.save()
            ca.kyprofile.is_ca = True
            ca.kyprofile.save()
            CASheetUpdate(ca)
            #messages.success(request,'CA registration successful, your CA id is '+ ca.caId +'',fail_silently=True)

            return HttpResponseRedirect('/profile')
        else:
            messages.warning(request,'invalid form', fail_silently=True)
    else:
        return render(request,template_name,context)


@csrf_exempt
def message(request):
    if request.method == "POST":
        print 'got a requesst'
        post = request.POST
        email = post.get('email')
        number = post.get('number')
        name = post.get('name')
        message = post.get('msg')

        Message.objects.create(name=name,email=email,mobileNumber=number,message=message)
        # messages.success(request,"Message recorded!, we'll contact you soon",fail_silently=True)
        response_data = {}

    else:
        raise Http404('not allowed')


@login_required(login_url='/form')
def DashboardView(request):
    template_name = 'dashboard.html'
    context = context_call(request)
    return render(request,template_name,context)

def ProfileView(request):
    template_name = 'profile.html'
    kyprofile = request.user.kyprofile
    if request.method == "GET":
        kydata = {
            'name':request.user.first_name,
            'mobileNumber': kyprofile.mobileNumber,
        }

        choosen = False
        try:
            if kyprofile.caprofile.isChoosen:
                choosen = True
        except Exception as e:
            pass

        context = {
            'choosen' : choosen,
        'kyprofile': kyprofile,
        'KyProfileEditForm':KyProfileEditForm(initial=kydata),
        }

        if choosen:
            ca = CAProfile.objects.get(kyprofile=kyprofile)
            cadata = {
                'whatsappNumber': ca.whatsappNumber,
                'postalAddress': ca.postalAddress,
                'pincode': ca.pincode
                }
            context['CAProfileEditForm'] = CAProfileEditForm(initial=cadata)
        return render(request,template_name,context)

    if request.method == "POST":
        post = request.POST

        ky = KYProfile.objects.get(user=request.user)
        ky.user.first_name = post.get('name')
        ky.mobileNumber = post.get('mobileNumber')
        ky.sex = post.get('sex')
        ky.year = post.get('year')
        ky.save()
        ky.user.save()
        if kyprofile.is_ca:
            whatsappNumber = post.get('whatsappNumber')
            postalAddress = post.get('postalAddress')
            pincode = post.get('pincode')
            ca = CAProfile.objects.get(kyprofile=kyprofile)
            ca.whatsappNumber = whatsappNumber
            ca.postalAddress = postalAddress
            ca.pincode = pincode
            ca.save()

        messages.success(request,'Profile successfully Updated!', fail_silently=True)
        return redirect('/profile')



def LogoutView(request):
    logout(request)
    return redirect('/')


@csrf_exempt
def forgotPassword(request):
    if request.user.is_authenticated():
        return redirect('/profile')
    if request.method == 'POST':
        email = request.POST.get("email")
        try:
            user = User.objects.get(email = email)
            # if user.is_active is False:
            #     messages.warning(request,"Please confirm your email first!")
            #     return redirect('/login')
        except:
            messages.warning(request, "Invalid Email!")
            return redirect('/forgotPass')

        subject = "Reset Password"
        forgotPassKey = 'asljdkflasjkdf' + email + 'jalfdjskdjf'
        forgotPassKey = str(hash(forgotPassKey))
        try:
            key = Key.objects.get(kyprofile = user.kyprofile)
            key.forgotPassKey = forgotPassKey
            key.save()
        except:
            key = Key(kyprofile = user.kyprofile, forgotPassKey = forgotPassKey)
            key.save()

        body = "Please Cick on the following link to reset your Password for Kashiyatra'17.\n\n"
        body += server + "resetPass/" + forgotPassKey
        try:
            if send_email(subject, body, email):
                messages.success(request, "Password Reset link sent to your Email.")
                return redirect('/form')
        except:
            messages.warning(request, "Email couldn't  be send, Retry please!")
            return redirect('/forgotPass')
    elif request.method == 'GET':
        return render(request,'forgotpass.html', {})
    else:
		raise Http404('NOT ALLOWED')



@csrf_exempt
def resetPass(request,forgotPassKey):
    if request.method == 'GET':
        try:
            key = Key.objects.get(forgotPassKey = int(forgotPassKey))
            return render(request,"reset.html")
        except:
            messages.warning(request,'Invalid Url!')
            return redirect('/form')

    elif request.method == "POST":
        post = request.POST
        try:
            key = Key.objects.get(forgotPassKey=forgotPassKey)
            kyprofile = key.kyprofile
            password1 = post.get('password1')
            password2 = post.get('password2')
            if password1 == password2:
                kyprofile.user.set_password(password1)
                kyprofile.user.save()
                messages.success(request,'password set successfully!',fail_silently=True)
                return redirect('/form')
            else:
                messages.warning(request, "passwords didn't match!")
                url = server + "resetPass/" + str(forgotPassKey)
                return redirect(url)
        except Exception as e:
            return HttpResponse(e)
            # raise Http404('Not allowed')




@login_required(login_url = "/form")
def changePass(request):
    template_name = 'passwordChange.html'
    context = {
        'form':PasswordChangeForm(),
    }
    if request.method == 'POST':
        post = request.POST
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            oldPassword = post.get('oldPassword')
            password1 = post.get('password1')
            password2 = post.get('password2')
            if password1 == password2 :
                user = authenticate(username=request.user.email,password=oldPassword)
                print user,oldPassword
                if user is not None:
                    request.user.set_password(password1)
                    request.user.save()
                    user = authenticate(username=request.user.email,password=password1)
                    login(request,user)
                    messages.success(request,'Password successfully set!',fail_silently=True)
                    return redirect('/profile')
                else:
                    messages.warning(request,'Wrong old password!',fail_silently=True)
                    return redirect('/changePass')

            else:
                messages.warning(request,"Passwords didn't match!!",fail_silently=True)
                return redirect('/changePass')
    else:
        return render(request, template_name, context)
import os
from django.views.static import serve

def rulebook(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(BASE_DIR, 'Pdfs/rulebook.pdf')
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


def infobrochure(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(BASE_DIR, 'Pdfs/infobrochure.pdf')
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
