from rest_framework import serializers
from .models import  UserTeam
class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = UserTeam
      fields = "__all__"