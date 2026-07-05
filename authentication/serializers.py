# authentication/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
import re


class SignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'image']

    def validate_username(self, value):
        if not re.match(r'^[A-Za-z]+$', value):
            raise serializers.ValidationError(
                "Only letters allowed in username"
            )
        return value

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords do not match"}
            )
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        image = validated_data.pop('image', None)

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1']
        )

        # seller create handled in view
        return user