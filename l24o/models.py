from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Serial(models.Model):
    name = models.TextField()
    publish_date = models.DateField()
    url = models.TextField()

class Video(models.Model):
    serial = models.ForeignKey(to=Serial)
    season = models.DecimalField()
    v_of_season = models.DecimalField()