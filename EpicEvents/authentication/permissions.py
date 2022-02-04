from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user
from .models import UserTeam
from .serializers import UserTeamSerializer
from CRMapp.models import Client, Contract, Event
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
        if request.user.team == "Sale":
            return True
        else:
            return False
    def has_object_permission(self, request, view, obj):
        if request.user.team == "Sale":
            if request.method in SAFE_METHODS:
                return True
            else:
                # Trouver comment faire pour les events
                if type(obj) == Client or type(obj) == Contract:
                    if obj.sales_contact == request.user:
                        return True
                    else:
                        return False
                # Vérifier si ça fonctionne
                elif type(obj) == Event:
                    client = obj.client
                    if client.sales_contact == request.user:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False


class IsUserSupport(BasePermission):
    # Les requetes POST ne sont gérés que par has_permission
    # (logique car dans vue de liste et non pas de détail)
    def has_permission(self, request, view):
        if request.user.team == "Support":
            if request.method == 'POST':
                return False
            else:
                return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.team == "Support":
            if request.method in SAFE_METHODS:
                return True
            else:
                if type(obj) == Event:
                    if obj.support_contact == request.user:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False


class IsUserManagement(BasePermission):
    def has_permission(self, request, view):
        if request.user.team == "Management":
            if request.method == 'POST':
                if view.serializer_class == UserTeamSerializer:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    def has_object_permission(self, request, view, obj):
        if request.user.team == "Management":
            return True
        else:
            return False