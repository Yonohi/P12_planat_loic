from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user
from .models import UserSale, UserSupport, UserManagement
from django.contrib.auth.models import User


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


# a modifier
"""class IsUserManagement(BasePermission):
    def has_permission(self, request, view):
        user = get_user(request)
        if type(user) is UserManagement:
            if request.method in SAFE_METHODS:
                return True
            else:
                return False
        else:
            return False
    pass"""


class IsUserSale(BasePermission):
    def has_permission(self, request, view):
        user = get_user(request)
        if user in UserSale.objects.all():
            return True
        else:
            return False


class IsUserSupport(BasePermission):
    pass