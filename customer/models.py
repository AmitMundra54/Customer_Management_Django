# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
from core.models import User, Organisation


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer')
    is_individual = models.BooleanField()


class Company(models.Model):
    company = models.OneToOneField(Organisation)
    rating = models.CharField(max_length=5,null=True,blank=True)


class Product(models.Model):
    product_name = models.CharField(max_length=127)
    price = models.CharField(max_length=31, null=True, blank=True)
    variant = models.CharField(max_length=127, null=True, blank=True)
    tag = models.CharField(max_length=31, blank=True)
    quality = models.ForeignKey(max_length=127, null=True, blank=True)
    material = models.CharField(max_length=127, null=True, blank=True)
    company = models.ForeignKey(Company, related_name="product_company")


class ProductType(models.Model):
    type = models.ForeignKey(Category, related_name='product_type')


class Category(models.Model):
    product_category = models.ForeignKey(Product, related_name='category')


class Order(models.Model):
    order_no = models.IntegerField
    product = models.ForeignKey(Product)
    type = models.CharField(max_length=31, choices=[('Instant','Instant'),('Easy','Easy')])
    placed_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, related_name='orders')
    quantity = models.IntegerField()
    status = models.CharField(choices=[('delivered','delivered'),('dispatched','dispatched')])
    discount = models.CharField(max_length=6, null=True, blank=True)







