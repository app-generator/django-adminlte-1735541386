# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Endpoints(models.Model):

    #__Endpoints_FIELDS__
    hostname = models.TextField(max_length=255, null=True, blank=True)
    crowdstrike installed = models.BooleanField()
    ms installed = models.BooleanField()
    dg installed = models.BooleanField()
    mcafee installed = models.BooleanField()
    current windows version = models.TextField(max_length=255, null=True, blank=True)
    is it active in sccm = models.TextField(max_length=255, null=True, blank=True)
    last seen online = models.DateTimeField(blank=True, null=True, default=timezone.now)
    change since last inventoried = models.TextField(max_length=255, null=True, blank=True)

    #__Endpoints_FIELDS__END

    class Meta:
        verbose_name        = _("Endpoints")
        verbose_name_plural = _("Endpoints")



#__MODELS__END
