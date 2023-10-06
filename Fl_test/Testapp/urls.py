from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('fl_data/', views.fl_data, name="fl_data"),
]
