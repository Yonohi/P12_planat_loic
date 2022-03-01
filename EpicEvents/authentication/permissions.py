from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user
from .serializers import UserTeamSerializer
from CRMapp.models import Client, Contract, Event
import datetime


class IsLogged(BasePermission):
    message = 'Vous n\'avez pas la permission d\'effectuer cette action. ' \
              'Vous n\'êtes pas connecté.'

    def has_permission(self, request, view):
        user = get_user(request)
        if type(user) is AnonymousUser:
            return False
        else:
            return True


class IsTeamSale(BasePermission):
    def has_permission(self, request, view):
        if request.user.team == "Sale":
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.team == "Sale":
            # On accepte les modifications seulement si l'utilisateur est
            # en lien avec l'instance
            if type(obj) == Client or type(obj) == Contract:
                if obj.sales_contact == request.user:
                    return True
                else:
                    return False
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


class IsTeamSupport(BasePermission):
    def has_permission(self, request, view):
        if request.user.team == "Support":
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.team == "Support":
            if type(obj) == Event:
                if obj.support_contact == request.user:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


class IsTeamManagement(BasePermission):
    def has_permission(self, request, view):
        if request.user.team == "Management":
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.team == "Management":
            return True
        else:
            return False


class EventInProgress(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            if type(obj) == Event:
                # Mettre USE_TZ à False dans settings sinon erreur
                if obj.event_date >= datetime.datetime.today():
                    return True
                else:
                    return False
            else:
                return False
