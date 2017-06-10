import requests
import csv
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
application = get_wsgi_application()

from django.contrib.auth.models import User
from KYusers.models import CAProfile, KYProfile, College


for col in College.objects.all():
    count = KYProfile.objects.filter(college=col).count()
    col.regCount = count
    col.save()
    print str(col) + 'Done!'
