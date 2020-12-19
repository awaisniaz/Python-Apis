from django.shortcuts import render
from django.contrib.auth.models import UserRegistration
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.


class UserView(viewsets.ModelViewSet):
    data = UserRegistration.objects.all()
    Userserializer = UserRegistration
    permissions = [permissions.IsAuthenticated]

