from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from .models import Client, Contract, ContractStatus, Event, EventStatus
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ClientSerializer(serializers.ModelSerializer):
    sales_contact = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    updated_at = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'company_name', 'email',
                  'phone', 'mobile', 'client_type', 'sales_contact',
                  'created_at', 'updated_at']


class ContractSerializer(serializers.ModelSerializer):

    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    sales_contact = serializers.PrimaryKeyRelatedField(read_only=True)
    status = serializers.PrimaryKeyRelatedField(queryset=ContractStatus.objects.all())
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    updated_at = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Contract
        fields = ['payment_due_at', 'amount', 'status', 'client',
                  'sales_contact', 'event', 'created_at', 'updated_at']


class EventSerializer(serializers.ModelSerializer):

    updated_at = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    status = serializers.PrimaryKeyRelatedField(queryset=EventStatus.objects.all())
    support_contact = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Event
        fields = '__all__'
