from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
application = get_wsgi_application()
# send_mail("Your Subject", "This is a simple text email body.",
#   "Yamil Asusta <hello@yamilasusta.com>", ["yamil@sendgrid.com"])
# from sendgrid import *
# from sendgrid.helpers.mail import *

# or
# attachment = Attachment()
# attachment.set_content("TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gQ3JhcyBwdW12")
# attachment.set_type("application/pdf")
# attachment.set_filename("balance_001.pdf")
# attachment.set_disposition("attachment")
# attachment.set_content_id("Balance Sheet")
to_list = ["rishabh.agrahari.eee15@iitbhu.ac.in","siddharth.agrawal.che14@iitbhu.ac.in", "sankalp.gupta.che14@itbhu.ac.in",]
mail = EmailMultiAlternatives(
  subject="test mail",
  body="This is a simple text email body.",
  from_email="Kashiyatra <kashiyatra@iitbhu.ac.in>",
  to=None,
  bcc=to_list,
  headers={"Reply-To": "kashiyatra@iitbhu.ac.in"},
)
# attachment = open("_mail.py", 'rb')
# mail.attach('filename.pdf', attachment.read(), 'text/plain')
mail.attach_file('/media/ags/DATA/MY_PORTALS/KY/kashiyatra/_mail.py')
mail.send()
