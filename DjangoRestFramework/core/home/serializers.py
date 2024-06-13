from rest_framework import serializers
from .models import Person, Color
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data["username"]:
            if User.objects.filter(username=data["username"]).exists():
                raise serializers.ValidationError("Username has been taken")
        if data["email"]:
            if User.objects.filter(email=data["email"]).exists():
                raise serializers.ValidationError("Email has been taken")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        return validated_data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["color_name"]


class PersonSerializer(serializers.ModelSerializer):
    # color = ColorSerializer()

    class Meta:
        model = Person
        fields = "__all__"

    def validate(self, data):
        special_chars = "!@#$%^&*()<>?/=-_+,"
        if any(c in special_chars for c in data["name"]):
            raise serializers.ValidationError("Name can not contain special chars")
        if data["age"] < 18:
            raise serializers.ValidationError("Age should be greater than 18")
        return data
