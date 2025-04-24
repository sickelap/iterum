from apps.inventory.models import Appliance
from django import template
from django.shortcuts import get_object_or_404

register = template.Library()


@register.inclusion_tag("components/header_card.html")
def header_card(title, user):
    return {"title": title, "user": user}


@register.inclusion_tag("components/inventory_list.html")
def inventory_list(appliance, inventory_items):
    return {"appliance": appliance, "inventory_items": inventory_items}


@register.inclusion_tag("components/appliance_details.html")
def appliance_details(item):
    return {"item": item}


@register.inclusion_tag("components/location_details.html")
def location_details(item):
    return {"item": item}


# TODO: remoce (used for dev)
# @register.inclusion_tag("components/order_replacement_form.html")
# def order_replacement_popup(appliance_id, replacement_id):
#     appliance = get_object_or_404(Appliance, pk=appliance_id)
#     replacement = get_object_or_404(Appliance, pk=replacement_id)
#     location = appliance.location
#     return {
#         "appliance": appliance,
#         "replacement": replacement,
#         "location": location,
#         "minute_options": ["00", "15", "30", "45"],
#         "selected_minutes": "00",
#         "hour_options": range(0, 23),
#         "selected_hour": 10,
#     }
