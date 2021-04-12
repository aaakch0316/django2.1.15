from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from .models import MyUser

User = get_user_model()

class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    # username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    phone_number = serializers.CharField()
    address = serializers.CharField()
    items_of_interest = serializers.CharField()
    job = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            # username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
            items_of_interest=validated_data['items_of_interest'],
            job=validated_data['job']
        )
        user.set_password(validated_data['password'])

        user.save()
        return user