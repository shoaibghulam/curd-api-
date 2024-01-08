from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)
    



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class AboutSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = About
        fields = ['id', 'first_name', 'last_name',  'Dob', 'Contact', 'Address', 'updated_at', 'created_at', 'user']

    # def create(self, validated_data):
    #     user_data = validated_data.pop('user_id')
    #     user = User.objects.create(**user_data)
    #     about = About.objects.create(user=user, **validated_data)
    #     return about