from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from .models import Client
from .serializers import ClientSerializer
from .permissions import IsSalesUser, IsClientOwner


class ListCreateClient(ListCreateAPIView):
    permission_classes = (IsSalesUser | IsAdminUser,)
    serializer_class = ClientSerializer

    def get_queryset(self):
        '''Get only the list of clients of the user.'''
        user = self.request.user
        return Client.objects.filter(sales_contact=user)

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
    permission_classes = (IsSalesUser, IsClientOwner, )
