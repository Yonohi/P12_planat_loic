from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserTeam
from .serializers import UserTeamSerializer
from .permissions import IsLogged, IsUserManagement, IsTeamManagement
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserTeamViewSet(viewsets.ModelViewSet):
    queryset = UserTeam.objects.exclude(username='NoSupport')
    serializer_class = UserTeamSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['username']
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated, IsLogged, IsTeamManagement]


class UserTeamSaleViewSet(viewsets.ModelViewSet):
    queryset = UserTeam.objects.filter(team='Sale')
    serializer_class = UserTeamSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['username']
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated, IsLogged, IsTeamManagement]


class UserTeamSupportViewSet(viewsets.ModelViewSet):
    queryset = UserTeam.objects.filter(team='Support').exclude(username='NoSupport')
    serializer_class = UserTeamSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['username']
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated, IsLogged, IsTeamManagement]


class UserTeamManagementViewSet(viewsets.ModelViewSet):
    queryset = UserTeam.objects.filter(team='Management')
    serializer_class = UserTeamSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['username']
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated, IsLogged, IsTeamManagement]