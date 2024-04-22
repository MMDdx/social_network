import uuid

from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=20)
    abbr = models.CharField(max_length=5)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        db_table = 'countries'

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(unique=True, blank=True, null=True)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True)


class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4
    DEVICE_CHOICES = (
        (DEVICE_WEB, 'web'),
        (DEVICE_IOS, 'ios'),
        (DEVICE_ANDROID, 'android'),
        (DEVICE_PC, 'pc'),
    )
    user = models.ForeignKey(to=User, related_name='devices', on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device uuid', null=True)
    device_type = models.SmallIntegerField(choices=DEVICE_CHOICES, default=DEVICE_WEB)
    device_os = models.CharField('device os', max_length=10, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

