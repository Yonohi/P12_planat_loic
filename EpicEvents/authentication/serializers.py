from rest_framework import serializers
from .models import  UserTeam
import django.contrib.auth.password_validation as validators


class UserTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTeam
        fields = ['username', 'password', 'team']

    # create_user to have the hash
    def create(self, validated_data):
        user = UserTeam.objects.create_user(**validated_data)
        return user

    # password not check with create_user, need the following code
    @staticmethod
    def validate_password(data):
        validators.validate_password(password=data, user=UserTeam)
        return data