import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
application = get_wsgi_application()
# import django
# django.setup()
import csv
from KYusers.models import College

with open('b.csv','rb') as f:
    data = csv.reader(f)
    for row in data:
        College(collegeName=row[1]).save()
        print row[1]
        # college = College.objects.create(collegeName=row[1],collegeId='')
        # college.save()
