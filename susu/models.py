from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    acc_num = models.CharField(max_length=60, unique=True)
    next_of_kin = models.CharField(max_length=150, blank=True)
    next_of_kin_phone = models.CharField(max_length=60, blank=True)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __unicode__(self):
        return self.acc_num


class Voucher(models.Model):
    num = models.CharField(max_length=60, unique=True)
    value = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    used = models.BooleanField(default=False)
    date_created = models.DateField()
    date_used = models.DateField(blank=True, null=True)
    account = models.ForeignKey(Account, related_name='voucher_account', null=True, blank=True, default=None)

    def __unicode__(self):
        return self.num




class Member(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=60, null=False, blank=False)
    nationality = models.CharField(max_length=90, null=True, blank=True)
    address = models.CharField(max_length=150, blank=True)
    account = models.ForeignKey(Account, related_name='member_account', null=True, blank=True, default=None)
    mem_types = (
        ('m', 'manager'),
        ('a', 'agent'),
        ('c', 'client')
    )
    role = models.CharField(max_length=1, choices=mem_types)

    def __unicode__(self):
        return self.user.username




