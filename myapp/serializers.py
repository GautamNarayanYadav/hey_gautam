from rest_framework import serializers
from .models import MainPage, Contact


class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"
        read_only_fields = ["created_at"]
