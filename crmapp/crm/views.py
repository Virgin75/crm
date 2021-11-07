from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from .models import Client
from .serializers import ClientSerializer
from .permissions import IsSalesUser


class CreateClient(ListCreateAPIView):
    permission_classes = (IsSalesUser | IsAdminUser,)
    serializer_class = ClientSerializer

    def get_queryset(self):
        '''Get only the list of clients of the user.'''
        user = self.request.user
        return Client.objects.filter(sales_contact=user)

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


class ClientDetail(APIView):
    """
    Retrieve, update a client instance.
    """

    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
