from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.DroneView.as_view())
]