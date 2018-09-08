from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import SubmitDroneForm
from .models import Drone

class DroneView(View):
    def get(self, request, *args, **kwargs):
        data_form = SubmitDroneForm()
        context = {
            "form": data_form
        }
        return render(request, "drone/drone_input.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitDroneForm(request.POST)
        if form.is_valid():
            new_drone = form.save()
            new_drone.save()
            new_drone.connect()

        context = {"form": form}
        return render(request, "drone/drone_input.html", context)
