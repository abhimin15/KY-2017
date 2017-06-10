from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator

# Create your models here.

class Sponser(models.Model):
    sponserTag = models.CharField(max_length=250)
    sponserName = models.CharField(max_length=250)
    photo = models.TextField(validators=[URLValidator()],blank=True,null = True)

    def __unicode__(str):
        return '%s' % sponserName
