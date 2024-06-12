from rest_framework import serializers
from .models import Person, Color


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["color_name"]


class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer()

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
