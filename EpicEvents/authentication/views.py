from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserTeam
from .serializers import UserTeamSerializer
from .permissions import IsLogged, IsUserManagement, IsTeamManagement


class UserTeamViewSet(viewsets.ModelViewSet):
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer
    permission_classes = [IsAuthenticated, IsLogged, IsTeamManagement]