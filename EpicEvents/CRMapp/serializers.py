from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Client, Contract, Event
from authentication.serializers import UserTeamSerializer


class ClientSerializer(serializers.ModelSerializer):
    # Permet d'avoir le str() de l'instance de sales_contact au lieu de l'id
    sales_contact = serializers.StringRelatedField()
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created', 'date_updated', 'sales_contact', 'client_status']


class ContractSerializer(serializers.ModelSerializer):
    sales_contact = serializers.StringRelatedField()
    client = serializers.StringRelatedField()
    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client', 'date_created', 'date_updated', 'status', 'amount', 'payment_due']
    # On met automatiquement à Existant le statut du client ayant un contrat
    def create(self, validated_data):
        contract = Contract.objects.create(**validated_data)
        client = Client.objects.get(id=validated_data['client'].id)
        client.client_status = 'Existant'
        client.save()
        return contract

class EventSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    support_contact = serializers.StringRelatedField()
    event_status = serializers.StringRelatedField()
    class Meta:
        model = Event
        fields = ['id', 'client', 'date_created', 'date_updated', 'support_contact', 'event_status', 'attendees', 'event_date', 'notes']


class MyClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile',
                  'company_name', 'date_created', 'date_updated',
                  'sales_contact', 'client_status']
        read_only_fields = ['sales_contact']
    def create(self, validated_data):
        client = Client.objects.create(sales_contact=self.context['user'], **validated_data)
        return client