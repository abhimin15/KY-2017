import requests
import csv
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
application = get_wsgi_application()

from django.contrib.auth.models import User
from KYusers.models import CAProfile, KYProfile, College

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


kyprofiles = KYProfile.objects.all()


with open('ca_data.csv','rb') as f:
    data = csv.reader(f)
    for row in data:
        name, email = row[0], row[3]
        college = row[4]
        mn, wn = row[5], row[6]
        postalAddress = row[7]
        fblink = row[8]
        if mn:
            try:
                user = User.objects.get(username=email, email= email, first_name=name)
                kyprofile = KYProfile.objects.get(user = user)
                print user, kyprofile
                try:
                    caprofile = CAProfile(kyprofile=kyprofile,whatsappNumber=wn,postalAddress=postalAddress,fblink=fblink)
                    caprofile.save()
                    CASheetUpdate(caprofile)
                    print 'CAprofile Done!'
                    user.set_password(caprofile.kyprofile.mobileNumber)
                    user.save()
                    print '\nDONE !!!!!!!!!!\n'
                except Exception as e:
                    print e
            except Exception as e:
                print e
