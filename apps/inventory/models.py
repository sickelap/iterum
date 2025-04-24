import random
from datetime import datetime, timezone
from typing import cast

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class EfficiencyLevel(models.TextChoices):
    MODERATE = "Moderate", _("Moderate")
    GOOD = "Good", _("Good")
    HIGH = "High", _("High")
    VERY_HIGH = "Very High", _("Very High")


class ApplianceCategory(models.TextChoices):
    DISHWASHER = "Dishwasher", _("Dishwasher")
    EXTRACTOR = "Extractor", _("Extractor")
    FREEZER = "Freezer", _("Freezer")
    FRIDGE = "Refridgerator", _("Refridgerator")
    HOB = "Hob", _("Hob")
    WASHING_MACHINE = "Washing Machine", _("Washing Machine")


class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Location(models.Model):
    address1 = models.CharField("Buiding", max_length=255)
    address2 = models.CharField("Appartment", max_length=255)

    def __str__(self):
        count = cast(models.Manager, self.appliances).count()
        return f"{self.address1} {self.address2} (appliances: {count})"


class Appliance(models.Model):
    category = models.CharField(max_length=100, choices=ApplianceCategory.choices)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    efficiency = models.CharField(max_length=20, choices=EfficiencyLevel.choices)
    image = models.ImageField(upload_to="appliance_images/", null=True, blank=True)
    sku_image = models.ImageField(upload_to="sku_images/", null=True, blank=True)
    warranty_until = models.DateField(null=True, blank=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="appliances",
    )

    @property
    def within_warranty_period(self):
        return self.warranty_until < datetime.now(timezone.utc)

    @property
    def matching_score(self):
        return f"{random.randint(50, 100)}%"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.category})"


class ReplacementOrder(models.Model):
    appliance = models.ForeignKey(
        Appliance, on_delete=models.CASCADE, related_name="replacement_order"
    )
    replacement = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    requested_date = models.DateField()
    notify_tenant_email = models.EmailField()
    notify_tenant_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Replace {self.appliance} at {self.location}"
