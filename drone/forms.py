from django.forms import ModelForm
from drone.models import Drone

class SubmitDroneForm(ModelForm):
    class Meta:
        model = Drone
        fields = ['port']
