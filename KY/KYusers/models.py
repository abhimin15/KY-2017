from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator

year_choices = [
        (None, 'Year'),
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5,'Fifth'),
    ]
sex_choices = [
    (None,'Sex'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

class College(models.Model):
    collegeId = models.CharField(max_length=20,blank=True)
    collegeName = models.CharField(max_length=250)
    regCount = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.id is None:
            self.id =  self.__class__.objects.all().order_by("-id")[0].id + 1
            self.collegeId = '%03d' %(self.id)
        super(self.__class__, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.collegeName


class KYProfile(models.Model):
    user = models.OneToOneField(User)
    sex = models.CharField(max_length=10, choices=sex_choices,null=True,blank=True)
    year = models.PositiveSmallIntegerField(choices=year_choices,null=True,blank=True)
    mobileNumber = models.BigIntegerField(null=True,blank=True)
    college = models.ForeignKey(College)
    referralCode = models.CharField(max_length=20, null=True,blank=True) #should be caId of some CA.
    is_ca = models.BooleanField(default=False)
    kyId = models.CharField(max_length=20,blank=True)

    due = models.PositiveIntegerField(null=True, blank=True)
    discount = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            try:
                self.id =  self.__class__.objects.all().order_by("-id")[0].id + 1
            except:
                self.id = 1
            self.kyId = 'KY-%s-%03d' % (self.college.collegeId, self.id)
        super(self.__class__, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s - %s - %s" %(self.user.first_name, self.college.collegeName, self.kyId)

#every CA will have KYProfile. so no need to have college (name,add again)
class CAProfile(models.Model):
    kyprofile = models.OneToOneField(KYProfile)
    postalAddress = models.TextField()
    whatsappNumber = models.BigIntegerField(null=True,blank=True)
    pincode = models.PositiveIntegerField(null=True,blank=True)
    whyChooseYou = models.TextField(null=True,blank=True)
    fblink = models.CharField(max_length=300,validators=[URLValidator()], null=True,blank=True,)

    regs = models.ManyToManyField(KYProfile, blank=True, related_name='regs')
    regNum = models.PositiveIntegerField(default=0,null=True, blank=True) #no. of refered kyprofile.
    caId = models.CharField(max_length=20,blank=True,null=True) #to be set by publicity team
    isChoosen = models.BooleanField(default=False,)


    def __unicode__(self):
        return "%s - %s" %(self.kyprofile.user.first_name, self.caId)

class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    mobileNumber = models.BigIntegerField(null=True, blank=True)
    message = models.TextField()
    mark_read = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Key(models.Model):
    kyprofile = models.OneToOneField(KYProfile)
    forgotPassKey = models.CharField(max_length=250, null=True, blank=True)
    confirmationKey = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return '%s' %self.kyprofile
