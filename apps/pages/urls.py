from django.urls import path

from . import views

urlpatterns = [
    path("", views.replace),
    path(
        "fragments/order_replacement_form/<int:appliance_id>/<int:replacement_id>",
        views.order_replacement_form,
        name="order_replacement_form",
    ),
]
