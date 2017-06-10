# -*- coding: cp1252 -*-
import sendgrid
from sendgrid import SendGridClient
import csv
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KY.settings")
application = get_wsgi_application()
# client = sendgrid.SendGridClient("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")
# message = sendgrid.Mail()

content = '''
<html>
<head>
<h4>Greetings from IIT BHU!</h4>

<p>Your login Credentials for Kashiyatra official beta website are: <br>
Email : %s<br>
Password : %s <br>
Please login at http://kashiyatra.herokuapp.com/form to register in KY'17 events. <br> </p>
Kashiyatra comprises of the following competitions with a total of over 30 dynamic sub-events:
<ul>
<li>       <b>Abhinay</b> - A series of theatrical competitions showcasing the richness of this artform.</li>
<li>       <b>Natraj</b> - The Holy Grail of Dance events, organized in association with Hip Hop International.</li>
<li>       <b>Bandish</b> - A competition solely dedicated to Indian music.</li>
<li>       <b>Crosswindz</b> - One of the biggest rock and metal music festivals in India.</li>
<li>       <b>Samwaad</b> - A literary extravaganza encompassing everything from spoken to written activities.</li>
<li>       <b>Enquizta</b> - A relay of Quizzes across different genres. Recognized in the <b>Top 10 Quizzes in India.</b></li>
<li>       <b>Toolika</b> - Fine Arts Marathon to give creativity a reality.</li>
<li>       <b>Mirage</b> - The Fashion Show, graced with the likes of Miss Earth India Aaital Khosla and other bigwigs in the past.</li>
</ul>

<p>We believe in keeping our attendees at their feet at all times. A plethora of informal events coupled with the competitions consume your day while we leave the nights for the dazzling pro-nites to get you in the groove. Some of the acts which we have hosted in the past include <b>Coke Studio, Euphoria, Nikhil D' Souza, Sunburn, VH1 Supersonic, Lucky Ali</b> and Death Metal Bands like <b>Demonic Resurrection</b> and <b>Undying INC</b>. KY hosts and showcases different cultures every year with various International acts. <b>Will Flanagan, Nir Koren, Tiny Fingers, Ehud Segav</b> are some of the renowned artists from across borders which have dazzled the crowd at KY over the years.</p>

<p>All in all, Kashiyatra along with the serenity of Banaras, always deliver an enchanting experience. We look forward to host you here at IIT BHU!</p>


<p>For any queries, Contact:<br>
Sankalp Gupta: +91-9897668839  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Siddharth Agrawal: +91-9818803290,+91-7839305430</p>


Cheers!<br>
Team KY<br>
<br>
<a href="https://www.facebook.com/kashiyatra.iitbhu">Facebook</a>
<a href="https://www.instagram.com/kashiyatra_iitbhu/">Instagram</a>
<a href="https://twitter.com/KY_IITBHU">Twitter</a>
<a href="https://www.youtube.com/c/KashiyatraIITBHU">Youtube</a>
'''
from django.contrib.auth.models import User


for user in User.objects.all():
    pwd = hash(user.email)
    user.set_password(pwd)
    user.save()
    mail = EmailMultiAlternatives(
      subject="Kashiyatra'17, IIT (BHU), Varanasi",
      from_email="Kashiyatra <kashiyatra@iitbhu.ac.in>",
      to=[user.email],
      headers={"Reply-To": "kashiyatra@iitbhu.ac.in"},
    )
    mail.attach_alternative(content %(user.email, pwd ), "text/html")



    if user.email =='rishabh.ag342@gmail.com':
        mail.send()
