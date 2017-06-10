from django.contrib.auth.models import User
from django import forms
from KYusers.models import *

class RegisterForm(forms.ModelForm):

    name = forms.CharField(label="Name",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','placeholder':'Name',}))

    sex = forms.ChoiceField(widget=forms.Select(attrs={'class': 'sex','required':'true', 'placeholder':'Sex', }),choices=sex_choices,)

    year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'year', 'required':'true','placeholder':'Year', }),choices=year_choices,)

    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Email'}))

    password = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'password', 'placeholder':'Password', 'name': 'password'}))

    college = forms.CharField(label="College",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'text', 'placeholder':"College"}))

    mobileNumber = forms.IntegerField(label="Mobile Number",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'number', 'placeholder':"Mobile Number"}))

    referralCode = forms.CharField(label="Referral Code",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Referral code (optional)',}))

    class Meta:
        model = KYProfile
        fields = ['name','email','password','year','sex','college','mobileNumber','referralCode']
        exclude = ['user_id','user','profile_photo']



class LoginForm(forms.Form):
    email = forms.CharField(label="email",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email','required':'true', 'type':'text','name': 'email'}))
    password = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Password','required':'true', 'type':'password','name': 'password'}))

class CARegisterForm(forms.ModelForm):

    whatsappNumber = forms.IntegerField(label="Mobile Number",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'number', 'placeholder':"WhatsApp Number"}))

    postalAddress = forms.CharField(label="Postal Address",
                               widget=forms.Textarea(attrs={'class': 'form-control','type':'textarea','rows': '5', 'placeholder':"Postal Address"}))

    pincode = forms.IntegerField(label="Pincode",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'number', 'placeholder':"Pincode"}))

    fblink = forms.URLField(label="FB link",
                         widget=forms.URLInput(attrs={'class':'form-control','placeholder':'Facebook link'}))

    whyChooseYou = forms.CharField(label="Why You?",
                               widget=forms.Textarea(attrs={'class': 'form-control','type':'textarea','rows': '5', 'placeholder':"Why You?"}))

    class Meta:
        model = CAProfile
        fields = ['whatsappNumber','fblink','postalAddress','pincode','whyChooseYou']
        exclude = ['kyprofile']


class KyProfileEditForm(forms.Form):

    name = forms.CharField(label="Name",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','placeholder':'Name',}))

    sex = forms.ChoiceField(widget=forms.Select(attrs={'class': 'sex','required':'true', 'placeholder':'Sex', }),choices=sex_choices,)

    year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'year', 'required':'true','placeholder':'Year', }),choices=year_choices,)

    mobileNumber = forms.IntegerField(label="Mobile Number",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'number', 'placeholder':"Mobile Number"}))


class CAProfileEditForm(forms.Form):

    whatsappNumber = forms.IntegerField(label="WhatsApp Number",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'number', 'placeholder':"WhatsApp Number"}))

    postalAddress = forms.CharField(label="Postal Address",
                               widget=forms.Textarea(attrs={'class': 'form-control','required':'true','type':'textarea','rows': '5', 'placeholder':"Postal Address"}))

    pincode = forms.IntegerField(label="Pincode",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'number', 'placeholder':"Pincode"}))


class PasswordChangeForm(forms.Form):

    oldPassword = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Old password','required':'true', 'type':'password','name': 'oldPassword'}))

    password1 = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'New password','required':'true', 'type':'password','name': 'password1'}))

    password2 = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'New password (repeat)','required':'true', 'type':'password','name': 'password2'}))
