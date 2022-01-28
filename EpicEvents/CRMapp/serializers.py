from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Client, Contract, Event


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created', 'date_updated', 'sales_contact', 'payment_due']


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client', 'date_created', 'date_updated', 'status', 'amount']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'client', 'date_created', 'date_updated', 'support_contact', 'event_status', 'attendees', 'event_date', 'notes']

