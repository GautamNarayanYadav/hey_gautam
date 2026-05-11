from django.urls import (
    path,
    include
)

from rest_framework.routers import (
    DefaultRouter
)

from .views import *


router = DefaultRouter()

router.register(
    'contact',
    ContactViewSet,
    basename='contact'
)


urlpatterns = [

    path(
        'main-page/',
        MainPageAPIView.as_view(),
        name='main-page-api'
    ),

    path(
        '',
        include(router.urls)
    ),

]