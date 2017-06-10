import requests
# import os
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
# application = get_wsgi_application()
#
# from KYusers.models import CAProfile

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
    requests.post(url,data=dic)

#
# for caprofile in CAProfile.objects.all():
#     try:
#         SheetUpdate(caprofile)
#         print (caprofile)
#     except requests.exceptions.ConnectionError:
#         print ('ConnectionError')
