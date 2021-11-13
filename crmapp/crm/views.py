from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from datetime import datetime
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from .permissions import IsSalesUser, IsClientOwner, SalesCanCreateSupportCanList, IsSupportUser, IsEventOwner, IsOwner


class ListCreateClient(ListCreateAPIView):
    permission_classes = (IsSalesUser | IsAdminUser,)
    serializer_class = ClientSerializer

    def get_queryset(self):
        '''Get only the list of clients of the user.'''
        user = self.request.user
        queryset = Client.objects.filter(sales_contact=user)

        name = self.request.query_params.get('name')
        email = self.request.query_params.get('email')

        if name is not None:
            queryset = queryset.filter(last_name__icontains=name)
        if email is not None:
            queryset = queryset.filter(email__icontains=email)

        return queryset

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


class ClientDetail(RetrieveUpdateAPIView):
    """
    Retrieve or update a client instance.
    """
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsSalesUser | IsSupportUser, IsOwner, )


class ListCreateContract(ListCreateAPIView):
    permission_classes = (IsSalesUser,)
    serializer_class = ContractSerializer

    def get_queryset(self):
        '''Get only the list of contracts of the user's clients.'''
        user = self.request.user
        client_list = Client.objects.filter(sales_contact=user)
        queryset = Contract.objects.filter(client__in=client_list)

        client_name = self.request.query_params.get('client_name')
        client_email = self.request.query_params.get('client_email')
        amount_min = self.request.query_params.get('amount_min')
        amount_max = self.request.query_params.get('amount_max')
        # Expected date format in query params : 2021-12-31
        date_min = datetime.strptime(
            self.request.query_params.get('date_min'), '%Y-%m-%d'
        )
        date_max = datetime.strptime(
            self.request.query_params.get('date_max'), '%Y-%m-%d'
        )

        if client_name is not None:
            name_filter = Client.objects.filter(last_name__icontains=client_name)
            queryset = queryset.filter(client__in=name_filter)
        if client_email is not None:
            email_filter = Client.objects.filter(email__icontains=client_email)
            queryset = queryset.filter(client__in=email_filter)
        if amount_min is not None:
            queryset = queryset.filter(amount__gte=amount_min)
        if amount_max is not None:
            queryset = queryset.filter(amount__lte=amount_max)
        if date_min is not None and date_max is not None:
            queryset = queryset.filter(created_at__range=(date_min, date_max))

        return queryset

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


class ContractDetail(RetrieveUpdateAPIView):
    """
    Retrieve or update a contract instance.
    """
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = (IsSalesUser, IsClientOwner, )


class ListCreateEvent(ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = (SalesCanCreateSupportCanList, )

    def get_queryset(self):
        '''Get only the list of events attributed to the support user.'''
        queryset = Event.objects.filter(support_contact=self.request.user)

        client_name = self.request.query_params.get('client_name')
        client_email = self.request.query_params.get('client_email')
        # Expected date format in query params : 2021-12-31
        date_min = datetime.strptime(
            self.request.query_params.get('date_min'), '%Y-%m-%d'
        )
        date_max = datetime.strptime(
            self.request.query_params.get('date_max'), '%Y-%m-%d'
        )

        if client_name is not None:
            name_filter = Client.objects.filter(last_name__icontains=client_name)
            queryset = queryset.filter(client__in=name_filter)
        if client_email is not None:
            email_filter = Client.objects.filter(email__icontains=client_email)
            queryset = queryset.filter(client__in=email_filter)
        if date_min is not None and date_max is not None:
            queryset = queryset.filter(date__range=(date_min, date_max))

        return queryset


class EventDetail(RetrieveUpdateAPIView):
    """
    Retrieve or update an event instance.
    """
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsSupportUser, IsEventOwner)
