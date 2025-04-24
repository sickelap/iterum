from django.contrib import admin

from .models import Appliance, Location, ReplacementOrder, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "is_staff")
    search_fields = ("first_name", "last_name", "email", "username")
    list_filter = ("is_staff", "is_superuser", "is_active")


@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    list_display = ("category", "brand", "model", "warranty_until", "location")
    list_filter = ("category", "brand", "model")
    search_fields = ("category", "brand", "model")


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("address1", "address2")
    search_fields = ("address1", "address2")


@admin.register(ReplacementOrder)
class ReplacementOrderAdmin(admin.ModelAdmin):
    list_display = (
        "location",
        "appliance",
        "replacement",
        "requested_date",
        "requested_by",
        "notify_tenant_email",
        "notify_tenant_number",
    )
    list_filter = ("requested_date",)
    search_fields = (
        "location__address1",
        "current_appliance__model",
        "replacement_appliance__model",
        "notify_tenant_email",
    )
