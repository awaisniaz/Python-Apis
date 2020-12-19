from django.contrib.auth.models import UserRegistration
from rest_framework import serializers

class UserSeriliazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['Name','email']