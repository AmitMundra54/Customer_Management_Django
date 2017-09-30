# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models import fields
from datetime import datetime, date



# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=127)
    middle_name = models.CharField(max_length=127, null=True, blank=True)
    last_name = models.CharField(max_length=127)
    gender = models.CharField(choices=[('Male','Male'), ('Female','Female')], max_length=31)
    date_of_birth = fields.DateField(null=True, blank=True)
    personal_email = models.EmailField(null=True, blank=True)
    designation = models.CharField(max_length=215, null=True, blank=True)
    is_individual = models.BooleanField(default=True)
    # category = models.CharField(choices=[('student','student'),('customer','cunstomer'),('teacher','teacher')])

    def __unicode__(self):
        return "{} {}".format(self.first_name,self.last_name)



class Organisation(models.Model):
    user = models.ForeignKey(User, related_name="organisation")
    name = models.CharField(max_length=128, unique=True)
    type = models.CharField(choices=[("Private",'Private'),('Government','Government')], max_length=31, default="Private")
    company_email = models.EmailField(max_length=31,null=True,blank=True)
    # contact_no = models.ForeignKey(PhoneNumber, related_name="company_contact_no", null=True, blank=True)

    def __unicode__(self):
        return self.name


class Address(models.Model):
    user = models.ForeignKey(User, related_name="address")
    address = models.ForeignKey(Organisation, max_length=128,  related_name="organisationAddress", null=True, blank=True)
    city = models.CharField(max_length=127, null=True, blank=True)
    state = models.CharField(max_length=127, null=True, blank=True)
    postal_code = models.CharField(max_length=6)

    def __unicode__(self):
        return "{}".format(self.city)

class PhoneNumber(models.Model):
    user = models.ForeignKey(User, related_name="user_contact_no")
    phone_number = models.CharField(max_length=10)
    # organisation = models.ForeignKey(Organisation,)


    def __unicode__(self):
        return "{}".format(self.phone_number)


class Department(models.Model):
    user = models.ForeignKey(User,related_name="department")
    name = models.CharField(max_length=127)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):

        return self.name


class Role(models.Model):
    user = models.ForeignKey(User, related_name='role')
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True,blank=True)

    def __unicode__(self):
        return "{}".format(self.title)





