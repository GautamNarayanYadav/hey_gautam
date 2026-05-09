from django.urls import path
from .views import home, MainPageAPIView

urlpatterns = [
    path('', home),
    path('api/main-page/', MainPageAPIView.as_view()),
]
