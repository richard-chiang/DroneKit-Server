from django.db import models
from .vehicle import Vehicle

# Create your models here.
class Drone(models.Model):
    port = models.IntegerField()
    vehicle = Vehicle()

    def connect(self):
        self.vehicle.connect(self.port)

    def close(self):
        self.vehicle.close()