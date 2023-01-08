from django.urls import path
from . import views

urlpatterns = [
    path("",views.homeIdam, name="home")

]