from rest_framework import serializers
from .models import User, Protector

class ProtectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protector
        fields = ['id', 'name', 'phone', 'relation']

class UserSerializer(serializers.ModelSerializer):
    protectors = ProtectorSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'birth_date', 'gender', 'phone', 'preferences','weight', 'protectors']
