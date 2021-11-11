from rest_framework.permissions import BasePermission
from .models import Client, Contract


class IsSalesUser(BasePermission):
    # Allows access only to sales group members.
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(id=1):
            return True
        return False


class IsClientOwner(BasePermission):
    # Allow only sales' owner of the client to perform an action on client
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Client):
            if obj.sales_contact == request.user:
                return True
            return False
        elif isinstance(obj, Contract):
            print(obj.client.sales_contact)
            if obj.client.sales_contact == request.user:
                return True
            return False


class SalesCanCreateSupportCanList(BasePermission):
    # Allows access only to sales group members.
    def has_permission(self, request, view):
        # Sales user with POST request
        if request.user.groups.filter(id=1) and request.method == 'POST':
            return True
        # Support user with GET request
        if request.user.groups.filter(id=2) and request.method == 'GET':
            return True
        return False
