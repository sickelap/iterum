from apps.inventory.models import Appliance, Location
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render


@login_required
def replace(request):
    # simple queried for the view
    # production code would have proper filters
    location = Location.objects.first()
    appliance = Appliance.objects.filter(location__isnull=False).get()
    inventory_items = Appliance.objects.filter(location__isnull=True)

    context = {
        "location": location,
        "appliance": appliance,
        "inventory_items": inventory_items,
        "suggested_dates": ["15th Sept", "16th Sept", "17th Sept"],
        "selected_date": "17th Sept",
    }

    return render(request, "pages/replace.html", context=context)


@login_required
def order_replacement_form(request, appliance_id, replacement_id):
    appliance = get_object_or_404(Appliance, pk=appliance_id)
    replacement = get_object_or_404(Appliance, pk=replacement_id)
    context = {
        "appliance": appliance,
        "replacement": replacement,
        "location": appliance.location,
        "minute_options": ["00", "15", "30", "45"],
        "selected_minutes": "00",
        "hour_options": range(0, 23),
        "selected_hour": 10,
    }
    return render(request, "components/order_replacement_form.html", context=context)
