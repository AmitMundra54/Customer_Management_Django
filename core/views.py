# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets

from core.models import User
from core.serializer import UserReadSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserReadSerializer