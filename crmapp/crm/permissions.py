from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from .models import Client, Contract, Event


# Returns 404 instead of 403 forbidden for security reasons
class CustomForbidden(APIException):
    status_code = 404
    default_detail = "Page not found."


class IsSalesUser(BasePermission):
    # Allows access only to sales group members.
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(id=1):
            print('is sales')
            return True
        raise CustomForbidden


class IsSupportUser(BasePermission):
    # Allows access only to support group members.
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(id=2):
            return True
        raise CustomForbidden


class IsEventOwner(BasePermission):
    # Allows only support users marked as support_contact of the event to access it
    def has_object_permission(self, request, view, obj):
        if obj.support_contact == request.user:
            return True
        raise CustomForbidden


class IsClientOwner(BasePermission):
    # Allow only sales' owner of the client to perform an action on client
    def has_object_permission(self, request, view, obj):
        print('aaaz')
        if isinstance(obj, Client):
            print('aa')
            if obj.sales_contact == request.user:
                return True
            raise CustomForbidden
        elif isinstance(obj, Contract):
            print(obj.client.sales_contact)
            if obj.client.sales_contact == request.user:
                return True
            raise CustomForbidden


class IsOwner(BasePermission):
    # Allow only sales or support users in relation with a client to access it
    def has_object_permission(self, request, view, obj):
        # Sales user
        if request.user.groups.filter(id=1):
            if obj.sales_contact == request.user:
                return True
        # Support user
        if request.user.groups.filter(id=2):
            events_of_client = Event.objects.filter(client=obj)
            for event in events_of_client:
                if event.support_contact == request.user:
                    return True
        raise CustomForbidden


class SalesCanCreateSupportCanList(BasePermission):
    # Allows access only to sales group members.
    def has_permission(self, request, view):
        # Sales user with POST request
        if request.user.groups.filter(id=1) and request.method == 'POST':
            return True
        # Support user with GET request
        if request.user.groups.filter(id=2) and request.method == 'GET':
            return True
        raise CustomForbidden
