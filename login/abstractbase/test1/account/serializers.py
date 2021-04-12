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



# login
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None:
            return {
                'email': 'None'
            }
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': user.email,
            'token': jwt_token
        }

class UserSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'email': instance.email,
            # 'player_name': instance.player_name
        }
    # class Meta:
    #     model = MyUser
    #     fields = ['id', 'email']