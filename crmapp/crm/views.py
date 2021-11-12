from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
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
            queryset = queryset.filter(last_name__contains=name)
        if email is not None:
            queryset = queryset.filter(email__contains=email)

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
        return Contract.objects.filter(client__in=client_list)

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
        return Event.objects.filter(support_contact=self.request.user)


class EventDetail(RetrieveUpdateAPIView):
    """
    Retrieve or update an event instance.
    """
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsSupportUser, IsEventOwner)
