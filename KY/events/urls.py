from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from events.views import *

app_name='events'

urlpatterns = [

	url(r'^events$', eventPage, name= 'events_reg'),
	url(r'^contingent$', contingentRegistration, name= 'contingent_reg'),
	url(r'^events/teamRegister/(?P<eventName>[\w|\W]+)$', eventRegistration, name= 'events_reg'),
	url(r'^events/individualRegister/$', individualReg, name= 'ind_reg'),
	url(r'^regCheck/$', regCheckAjax, name= 'events_reg'),
	url(r'^dashboard/$', dashboard, name= 'dashboard'),
	url(r'^deregister/$', deregister, name= 'deregister'),

]
