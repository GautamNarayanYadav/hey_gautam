from django.contrib import admin
from .models import MainPage, Contact


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


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )