from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('index')


def home(request):
    return render(request,'axf/main/home/home.html')