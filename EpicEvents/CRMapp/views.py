from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .serializers import ClientSerializer, ContractSerializer, \
    EventSerializer, EventSerializerWithoutSupport, MyClientsSerializer
from .models import Client, Contract, Event
from authentication.permissions import IsLogged, \
    IsTeamSale, IsTeamSupport, IsTeamManagement, EventInProgress
from authentication.models import UserTeam


# Utililsation de | (maj+option+L) pour les permissions
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    # OrderingFilter me permet d'utiliser ordering et ainsi ordonner mon contenu
    # DjangoFilterBackend me permet d'utiliser des filtres dans l'url
    # (via filterset_fields)
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-date_updated']
    filterset_fields = '__all__'
    # La permission DjangoModelPermission nous permet d'utiliser les permissions en admin
    permission_classes = [IsAuthenticated,
                          IsLogged,
                          DjangoModelPermissions,
                          EventInProgress,
                          IsTeamSale | IsTeamSupport | IsTeamManagement]

    def get_serializer_class(self):
        if self.request.user.team == 'Management':
            serializer_class = EventSerializer
        else:
            serializer_class = EventSerializerWithoutSupport
        return serializer_class


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['last_name']
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated,
                          IsLogged,
                          DjangoModelPermissions,
                          IsTeamSale | IsTeamSupport | IsTeamManagement]


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-date_updated']
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated,
                          IsLogged,
                          DjangoModelPermissions,
                          IsTeamSale | IsTeamSupport | IsTeamManagement]


class MyClientsViewSet(viewsets.ModelViewSet):
    serializer_class = MyClientsSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['last_name']
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated,
                          IsLogged,
                          DjangoModelPermissions,
                          IsTeamSale]

    def get_queryset(self):
        user = self.request.user
        return Client.objects.filter(sales_contact=user)

    def create(self, request, *args, **kwargs):
        serializer_context = {
            'user': request.user,
        }
        serializer = MyClientsSerializer(data=request.data,
                                      context=serializer_context)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


class MyContractsViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-date_updated']
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated,
                          IsLogged,
                          DjangoModelPermissions,
                          IsTeamSale]

    def get_queryset(self):
        user = self.request.user
        return Contract.objects.filter(sales_contact=user)


class MyEventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-date_updated']
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated,
                          IsLogged,
                          DjangoModelPermissions,
                          IsTeamSupport]

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(support_contact=user)


class EventsWithoutSupportViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-date_updated']
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated,
                          IsLogged,
                          DjangoModelPermissions,
                          IsTeamManagement]

    def get_queryset(self):
        return Event.objects.filter(support_contact=UserTeam.objects.get(username='NoSupport'))
