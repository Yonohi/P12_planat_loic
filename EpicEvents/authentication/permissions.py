from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user
from .models import UserTeam
from django.contrib.auth.models import User


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
        if request.method is 'POST':
            return False
        else:
            return True
    def has_object_permission(self, request, view, obj):
        if request.user.team == "Sale":
            if request.method in SAFE_METHODS:
                return True
            else:
                # Ne marche pas
                if obj.sales_contact == request.user:
                    return True
                else:
                    return False
        else:
            return False


class IsUserSupport(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False
    def has_object_permission(self, request, view, obj):
        if request.user.team == "Support":
            return True
        else:
            return False


class IsUserManagement(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False
    def has_object_permission(self, request, view, obj):
        if request.user.team == "Management":
            return True
        else:
            return False