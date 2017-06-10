from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
application = get_wsgi_application()

# send_mail("Your Subject", "This is a simple text email body.",
#   "Yamil Asusta <hello@yamilasusta.com>", ["yamil@sendgrid.com"])

# or
mail = EmailMultiAlternatives(
  subject="test mail",
  body="This is a simple text email body.",
  from_email="Kashiyatra <kashiyatra@iitbhu.ac.in>",
  to=["rishabh.agrahari.eee15@iitbhu.ac.in"],
  headers={"Reply-To": "kashiyatra@iitbhu.ac.in"}
)
mail.attach_alternative("<p>This is a simple HTML email body</p>", "text/html")

mail.send()
