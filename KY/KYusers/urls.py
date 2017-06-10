from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from KYusers.views import *

app_name='kyusers'

urlpatterns = [

	url(r'^$', IndexView, name= 'index'),

	# url(r'^login$', LoginView, name= 'login'),

	# url(r'^register/$', RegisterView, name='register'),

	url(r'^ca-register/$', CARegisterView, name='caregister'),

	url(r'^form', FormView, name='form'),

	# url(r'^dashboard/$', DashboardView, name='dashboard'),

	url(r'^profile/$', ProfileView, name='profile'),

	url(r'^messages/$', message, name='messages'),

	url(r'^logout/$', LogoutView, name='logout'),

	url(r'^forgotPass/$', forgotPassword, name='forgotPassword'),
	url(r'^resetPass/(?P<forgotPassKey>[\w\-]+)/$', resetPass, name='resetPass'),
	url(r'^changePass/$', changePass, name='changePass'),
	url(r'^confirmEmail/(?P<confirmationKey>[\w\-]+)/$', confirmEmail, name='confirmEmail'),

	url(r'^rulebook/$', rulebook,),
	url(r'^infobrochure/$', infobrochure)
]
