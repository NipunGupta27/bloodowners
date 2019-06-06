from django.db import models
from django.utils import timezone


class Blood(models.Model):
    name = models.CharField(max_length=30)
    lname = models.CharField(max_length=200)
    mail = models.EmailField(max_length=50, null=False)
    phone = models.IntegerField()
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    password = models.CharField(max_length=50, null=True)
    last_updated = models.DateTimeField(timezone.now(), blank=True, null=True)
    bloodgrp = models.CharField(max_length=11)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return '{} - {}'.format(self.name, self.mail)


