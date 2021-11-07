from rest_framework.permissions import BasePermission


class IsSalesUser(BasePermission):
    # Allows access only to sales group members.
    def has_permission(self, request, view):
        print(request.user.groups)
        print(request.user)
        if request.user and request.user.groups.filter(id=1):
            return True
        return False


class IsClientOwner(BasePermission):
    # Allow only sales' owner of the client to perform an action on client
    def has_object_permission(self, request, view, obj):
        if obj.sales_contact == request.user:
            return True
        return False
