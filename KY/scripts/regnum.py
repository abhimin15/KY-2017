import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
application = get_wsgi_application()

from KYusers.models import CAProfile

all_ca = CAProfile.objects.all()

for ca in all_ca:
    ca.regNum = 0
    ca.save()
    print ca
