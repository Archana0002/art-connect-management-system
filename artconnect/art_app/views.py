from django.shortcuts import render
from . models import Usertable
# Create your views here.

def homepage(request):
    return render(request,'home.html')

def register(request):
    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('opassword')
        role=request.POST.get('role')

        Usertable_obj = Usertable(name=name,email=email,password=password,role=role)
        Usertable_obj.save()
    return render(request,'register.html')