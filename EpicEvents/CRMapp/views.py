from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsLogged, IsSafe
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from .models import Client, Contract, Event


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsLogged, IsSafe]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsLogged, IsSafe]


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsLogged, IsSafe]
