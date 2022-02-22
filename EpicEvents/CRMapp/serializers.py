from django.contrib.auth.models import User, Group
from rest_framework import serializers
from authentication.models import UserTeam
from .models import Client, Contract, Event, EventStatus
from authentication.serializers import UserTeamSerializer


class ClientSerializer(serializers.ModelSerializer):
    # A savoir StringRelatedField permet d'avoir le str() de l'instance de
    # sales_contact au lieu de l'id mais le rend en lecture seule pour avoir
    # quelque chose de semblable mais en lecture/écriture faire ce qui suit
    sales_contact = serializers.SlugRelatedField(slug_field='username', queryset=UserTeam.objects.filter(team='Sale'))
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created', 'date_updated', 'sales_contact', 'client_status']


class ContractSerializer(serializers.ModelSerializer):
    sales_contact = serializers.SlugRelatedField(slug_field='username', queryset=UserTeam.objects.filter(team='Sale'))
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
    support_contact = serializers.SlugRelatedField(slug_field='username', queryset=UserTeam.objects.filter(team='Support'))
    event_status = serializers.SlugRelatedField(slug_field='status', queryset=EventStatus.objects.all())
    class Meta:
        model = Event
        fields = ['id', 'client', 'date_created', 'date_updated', 'support_contact', 'event_status', 'attendees', 'event_date', 'notes']


class EventSerializerWithoutSupport(serializers.ModelSerializer):
    event_status = serializers.SlugRelatedField(slug_field='status', queryset=EventStatus.objects.all())
    class Meta:
        model = Event
        fields = ['id', 'client', 'date_created', 'date_updated', 'support_contact', 'event_status', 'attendees', 'event_date', 'notes']
        read_only_fields = ['support_contact']
    def create(self, validated_data):
        validated_data['support_contact'] = UserTeam.objects.get(username='NoSupport')
        event = Event.objects.create(**validated_data)
        return event

class MyClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile',
                  'company_name', 'date_created', 'date_updated',
                  'sales_contact', 'client_status']
        read_only_fields = ['sales_contact']
    # On peut se permettre ce create car l'utilisateur est forcément de la team Sale à cause des permissions
    def create(self, validated_data):
        client = Client.objects.create(sales_contact=self.context['user'], **validated_data)
        return client