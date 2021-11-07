from rest_framework.permissions import BasePermission


class IsSalesUser(BasePermission):
    # Allows access only to sales group members.
    def has_permission(self, request, view):
        print(request.user.groups)
        print(request.user)
        if request.user and request.user.groups.filter(id=1):
            return True
        return False
