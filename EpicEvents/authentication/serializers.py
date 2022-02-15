from rest_framework import serializers
from .models import  UserTeam
import django.contrib.auth.password_validation as validators
from django.contrib.auth.models import Group


class UserTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTeam
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'team']
        extra_kwargs = {'password': {'write_only': True}}

    # create_user pour le hash
    def create(self, validated_data):
        user = UserTeam.objects.create_user(**validated_data)
        vente = Group.objects.get(name='Vente')
        support = Group.objects.get(name='Support')
        gestion = Group.objects.get(name='Gestion')
        if user.team == "Sale":
            vente.user_set.add(user)
            vente.save()
        elif user.team == "Support":
            support.user_set.add(user)
            support.save()
        elif user.team == "Management":
            gestion.user_set.add(user)
            gestion.save()
        return user

    # password non vérifié avec create_user, nécessite le code suivant
    @staticmethod
    def validate_password(data):
        validators.validate_password(password=data, user=UserTeam)
        return data