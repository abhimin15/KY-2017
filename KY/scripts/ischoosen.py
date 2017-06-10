import requests
import csv
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
application = get_wsgi_application()

from django.contrib.auth.models import User
from KYusers.models import CAProfile, KYProfile, College

for ca in CAProfile.objects.all():
    if ca.caId:
        ca.isChoosen = True
        ca.save()
