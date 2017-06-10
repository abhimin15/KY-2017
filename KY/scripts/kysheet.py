import requests
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
application = get_wsgi_application()

from KYusers.models import KYProfile

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
    requests.post(url,data=dic)


# for kyprofile in KYProfile.objects.all():
#     try:
#         KYSheetUpdate(kyprofile)
#         print (kyprofile)
#     except requests.exceptions.ConnectionError:
#         print ('ConnectionError')
