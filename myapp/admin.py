from django.contrib import admin
from .models import MainPage


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "subtitle",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "subtitle",
    )