from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Category, Transaction


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "created_at"]


class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "category", "amount", "description", "date", "created_at"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirm"]

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError({"password": "password do not match."})

        return data

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
