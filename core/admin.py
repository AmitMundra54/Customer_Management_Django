# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from core.models import User, Role, Department, Organisation, Address, PhoneNumber, Customer
# from customermanagement.core.models import User

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Organisation)
admin.site.register(Address)
admin.site.register(PhoneNumber)
admin.site.register(Customer)

# Register your models here.
