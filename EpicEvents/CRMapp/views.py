from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from .models import Client, Contract, Event
from authentication.permissions import IsLogged, IsUserSale, IsUserSupport, IsUserManagement


#Utililsation de | (maj+option+L)
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsLogged, IsUserSale|IsUserSupport|IsUserManagement]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsLogged, IsUserSale|IsUserSupport|IsUserManagement]


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsLogged, IsUserSale|IsUserSupport|IsUserManagement]
