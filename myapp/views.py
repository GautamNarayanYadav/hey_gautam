from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MainPage
from .serializers import MainPageSerializer


def home(request):
    return render(
        request,
        "index.html"
    )


class MainPageAPIView(APIView):

    def get(self, request):

        page = MainPage.objects.filter(
            is_active=True
        ).first()

        serializer = MainPageSerializer(page)

        return Response(serializer.data)