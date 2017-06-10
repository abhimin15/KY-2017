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
<p><b>Indian Institute of Technology (Banaras Hindu University) Varanasi</b> presents its annual socio-cultural festival, <b>Kashiyatra</b>. Kashiyatra or KY, as we call it is a 3-day long extravaganza blending the disciplines of music, literature and arts into a fest of gargantuan proportions. Over the years, Kashiyatra has grown to become one of the <b>biggest galas of North India</b> with a footfall of 25,000+ college students spanning the entire nation. This edition, we bring you a <b><i>Millennial Reprise</i></b> to take you on a nostalgic ride to the unforgettable 90's.</p>

<p>We hereby take immense pleasure in welcoming you to the <b>35th Edition of KY</b>, from <b>20th-22nd January 2017</b>, in the heart of the cultural richness of <i>Banaras</i>.</p>

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

<p>For registrations, go to our beta-website http://kashiyatra.org. The main website will be up soon!<br>
The registration fee is Rs. 1200. The fee includes accommodation charges as well as passes for all the concerts.
</p>

<p>For any queries, Contact:<br>
Sankalp Gupta: +91-9897668839  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Siddharth Agrawal: +91-9818803290,+91-7839305430</p>

<p>PS: <b>Please find the attached Information Brochure, Events Poster, Rule Book and Official Invitation.</b></p>

Cheers!<br>
Team KY<br>
<br>
<a href="https://www.facebook.com/kashiyatra.iitbhu">Facebook</a>
<a href="https://www.instagram.com/kashiyatra_iitbhu/">Instagram</a>
<a href="https://twitter.com/KY_IITBHU">Twitter</a>
<a href="https://www.youtube.com/c/KashiyatraIITBHU">Youtube</a>
'''
to_list = []
with open('a.csv','rb') as f:
    data = csv.reader(f)
    for row in data:
        if row[0] :
            to_list.append(row[0])



# to_list = ["rishabh.agrahari.eee15@iitbhu.ac.in","kashiyatra@iitbhu.ac.in","siddharth.agrawal.che14@iitbhu.ac.in", "sankalp.gupta.che14@itbhu.ac.in",]
mail = EmailMultiAlternatives(
  subject="Kashiyatra'17, IIT (BHU), Varanasi",
  from_email="Kashiyatra <kashiyatra@iitbhu.ac.in>",
  to=['@'],
  bcc=to_list,
  headers={"Reply-To": "kashiyatra@iitbhu.ac.in"},
)
mail.attach_alternative(content, "text/html")


mail.attach_file('../attachment/Information_Brochure.pdf')
mail.attach_file('../attachment/Official_Invitation.pdf')
mail.attach_file('../attachment/Events_Poster.jpg')
mail.attach_file('../attachment/KY17_Rulebook.pdf')


mail.send()
