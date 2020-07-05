from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'axf/user/register/register.html')


def login(request):
    return render(request,'axf/user/login/login.html')