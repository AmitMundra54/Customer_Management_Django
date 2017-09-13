# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=127)
    middle_name = models.CharField(max_length=127, null=True, blank=True)
    last_name = models.CharField(max_length=127)
    gender = models.CharField(choices=[('Male','Male'), ('Female','Female')], max_length=31)
    date_of_birth = models.DateField(null=True, blank=True)
    personal_email = models.EmailField(null=True, blank=True)
    designation = models.CharField(max_length=215, null=True, blank=True)
    is_individual = models.BooleanField

    def __unicode__(self):
        return "{} {}".format(self.first_name,self.last_name)



class Address(models.Model):
    # user = models.ForeignKey(User, related_name="address")
    city = models.CharField(max_length=127, null=True, blank=True)
    state = models.CharField(max_length=127, null=True, blank=True)
    postal_code = models.IntegerField()

    def __unicode__(self):
        return "{}".format(self.city)


class Organisation(models.Model):
    user = models.ForeignKey(User, related_name="organisation")
    name = models.CharField(max_length=128, unique=True)
    address = models.ForeignKey(Address, max_length=128,  related_name="organisation", null=True, blank=True)

    def __unicode__(self):
        return self.name


class Department(models.Model):
    user = models.ForeignKey(User,related_name="department")
    name = models.CharField(max_length=127)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):

        return self.name


class PhoneNumber(models.Model):
    user = models.ForeignKey(User)
    phone_number = models.IntegerField()


    def __unicode__(self):
        return "{}".format(self.phone_number)


class Role(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __unicode__(self):
        return "{}".format(self.title)


class Customer(models.Model):
    user = models.OneToOneField(User)

    # def __unicode__(self):
    #     # print "##############", self
    #
    #     return "{} {}".format(self)




