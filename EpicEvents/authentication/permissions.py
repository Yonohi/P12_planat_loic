from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user

# a changer pas vraiment bien
class IsSafe(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True


class IsLogged(BasePermission):
    message = 'Vous n\'avez pas la permission d\'effectuer cette action. ' \
              'Vous n\'êtes pas connecté.'

    def has_permission(self, request, view):
        user = get_user(request)
        if type(user) is AnonymousUser:
            return False
        else:
            return True
