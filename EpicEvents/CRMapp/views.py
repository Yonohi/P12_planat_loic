from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from .models import Client, Contract, Event
from authentication.permissions import IsLogged, IsUserSale, IsUserSupport, IsUserManagement


#Utililsation de | (maj+option+L)
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    #permission_classes = [IsAuthenticated, IsLogged, IsUserSale|IsUserSupport|IsUserManagement]
    # la permission DjangoModelPermission nous permet d'utiliser les permissions en admin
    permission_classes = [IsAuthenticated, IsLogged, DjangoModelPermissions]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    #permission_classes = [IsAuthenticated, IsLogged, IsUserSale|IsUserSupport|IsUserManagement]
    permission_classes = [IsAuthenticated, IsLogged, DjangoModelPermissions]


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    #permission_classes = [IsAuthenticated, IsLogged, IsUserSale|IsUserSupport|IsUserManagement]
    permission_classes = [IsAuthenticated, IsLogged, DjangoModelPermissions]


class MyClientsViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsLogged, DjangoModelPermissions]
    def get_queryset(self):
        user = self.request.user
        return Client.objects.filter(sales_contact=user)