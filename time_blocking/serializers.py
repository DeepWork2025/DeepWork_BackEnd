from rest_framework import serializers
from .models import UserInfo
from django.contrib.auth.models import User


# ######## expose API ########
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    time_zone = serializers.CharField(required=False, allow_blank=True)
    language = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'time_zone', 'language']

    def create(self, validated_data):
        time_zone = validated_data.pop("time_zone", "")
        language = validated_data.pop("language", "")

        # store data into auth_user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        # store data into customized table: UserInfo
        user_info = UserInfo.objects.create(
            user=user,
            time_zone=time_zone,
            language=language,
        )

        return user_info
    
    # to show data that are allowed to access
    def to_representation(self, instance):
        return {
            "username": instance.user.username,
            "email": instance.user.email,
            "time_zone": instance.time_zone,
            "language": instance.language,
        }