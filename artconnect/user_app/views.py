from django.shortcuts import render

# Create your views here.

def user_dash(request):
    return render(request,'user_dash.html')
