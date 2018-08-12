from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, UserAccounts, SwiftCode, TransactionLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","email","username","password","first_name","is_staff","is_superuser")

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            is_staff=validated_data['is_staff'],
        )
        user.set_password(validated_data['password'])
        user.save()

        profile = UserProfile(user=user)
        profile.secret_key = validated_data['password']
        profile.save()


        Account = UserAccounts(user=user)
        Account.save()

        return user

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.is_staff = validated_data['is_staff']
        instance.set_password(validated_data['password'])
        instance.save()

        profile = UserProfile(user=instance)
        profile.secret_key = validated_data['password']
        profile.save()

        return instance

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    created_at = serializers.IntegerField(read_only=True)
    class Meta:
        model = UserProfile
        fields = "__all__"

class UserAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    created_at = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserAccounts
        fields = "__all__"

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UpdateAdminSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)

class SwiftCodeSerializer(serializers.ModelSerializer):
    created_at = serializers.IntegerField(read_only=True)
    user = UserSerializer
    class Meta:
        model = SwiftCode
        fields = "__all__"

class TransactionLogSerializer(serializers.ModelSerializer):
    created_at = serializers.IntegerField(read_only=True)
    user = UserSerializer

    class Meta:
        model = TransactionLog
        fields = "__all__"