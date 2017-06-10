import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
application = get_wsgi_application()
# import django
# django.setup()
import csv
from events.models import ParentEvent, Event

with open('Event.csv','rb') as f:
    data = csv.reader(f)
    for row in data:
        if row[1] == '' and row[2] == '':
            parentevent = ParentEvent.objects.create(categoryName=row[0])
            print parentevent
        else:
            event = Event.objects.create(eventName=row[0],
                                         minMembers=row[1],
                                         maxMembers=row[2],
                                         parentEvent=parentevent)
            print event
