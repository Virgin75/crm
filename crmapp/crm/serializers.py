from django.contrib.auth.models import User
from .models import Client
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'company_name', 'email',
                  'phone', 'mobile', 'client_type', 'sales_contact']
