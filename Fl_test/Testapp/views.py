from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

def index(request):
    return HttpResponse("test page")


def fl_data(request):
    data = models.FLtester.objects.all()
    return render(request, "fl_data.html", {"data_list":data})
