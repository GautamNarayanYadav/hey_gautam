from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class MainPageAPIView(APIView):

    def get(self, request):

        page = MainPage.objects.filter(
            is_active=True
        ).first()

        serializer = MainPageSerializer(page)

        return Response(serializer.data)


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['post']
