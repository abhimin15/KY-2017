import requests
import csv
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
application = get_wsgi_application()

from django.contrib.auth.models import User
from KYusers.models import CAProfile, KYProfile, College

def KYSheetUpdate(kyprofile):
    dic = {
    'kyId' : kyprofile.kyId,
    'name' : kyprofile.user.first_name,
    'email' : kyprofile.user.email,
    'college' : kyprofile.college.collegeName,
    'year' : kyprofile.year,
    'sex' : kyprofile.sex,
    'mobileNumber': kyprofile.mobileNumber,
    }

    url = 'https://script.google.com/macros/s/AKfycbxPGpG2CdhETEiUeHYP4qZPHyteAjoSnaK3MyQAm0FoQWhwSNPr/exec'

    try:
        requests.post(url,data=dic)
    except requests.exceptions.ConnectionError:
        print 'ConnectionError'


def CASheetUpdate(caprofile):
    dic = {
    'caId' : caprofile.caId,
    'name' : caprofile.kyprofile.user.first_name,
    'email' : caprofile.kyprofile.user.email,
    'college' : caprofile.kyprofile.college.collegeName,
    'year' : caprofile.kyprofile.year,
    'sex' : caprofile.kyprofile.sex,
    'mobileNumber': caprofile.kyprofile.mobileNumber,
    'whatsappNumber': caprofile.whatsappNumber,
    'postalAddress': caprofile.postalAddress,
    'pincode': caprofile.pincode,
    'whyChooseYou':caprofile.whyChooseYou,
    'fblink' : caprofile.fblink,
    }

    url = 'https://script.google.com/a/macros/itbhu.ac.in/s/AKfycbx302AbrVv-LaNY-E6Gj7_Zt4owgzbD54edhNx2xfAkqoZInble/exec'

    try:
        requests.post(url,data=dic)
    except requests.exceptions.ConnectionError:
        print 'ConnectionError'

with open('newcadata.csv','rb') as f:
    data = csv.reader(f)
    for row in data:
        caId = row[2]
        name, email = row[3], row[6]
        collegeName = row[7]
        mn = row[8]
        wn = row[9]
        postalAddress = row[10]
        fblink = row[11]
        if caId:
            if len(email)<30 :
                try:
                    user, created = User.objects.get_or_create(username=email)
                    if created:
                        print 'New user created!!'
                        college, created_ = College.objects.get_or_create(collegeName=collegeName)
                        kyprofile = KYProfile(user=user, mobileNumber=mn, college = college)
                        kyprofile.save()
                        user.email = email
                        user.first_name = name
                        user.set_password(caId)
                        user.save()
                        print 'kyprofile saved!'
                        KYSheetUpdate(kyprofile)
                        caprofile = CAProfile(kyprofile=kyprofile,whatsappNumber=wn,postalAddress=postalAddress,fblink=fblink,caId=caId)
                        caprofile.save()
                        print 'caprofile saved!'
                        CASheetUpdate(caprofile)
                        print 'New User Done!!!\n\n'

                    else:
                        print user
                        kyprofile = KYProfile.objects.get(user = user)
                        print user, kyprofile
                        caprofile = CAProfile(kyprofile=kyprofile,whatsappNumber=wn,postalAddress=postalAddress,fblink=fblink,caId=caId)
                        caprofile.save()
                        CASheetUpdate(caprofile)
                        print 'CAprofile Done!\n\n'
                        user.set_password(caprofile.caId)
                        user.save()
                except Exception as e:
                    print e
                    print 'EEEEEEEEEEEEEEXXXCEEPPPPPPPPPPPPPPTIOOOOOOOOOOOOOOOOOON'
            else:
                print email, name
                print 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'
