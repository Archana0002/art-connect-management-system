from django.shortcuts import render
from art_app.models import Arttable

# Create your views here.

def user_dash(request):
    art_list = Arttable.objects.all()

    # Pass the data to the template
    context = {
        'art_list': art_list
    }

    return render(request, 'user_dash.html', context)

def digital_dash(request):
    art_list = Arttable.objects.filter(arttype="2").all()

    # Pass the data to the template
    context = {
        'art_list': art_list
    }

    return render(request, 'user_dash.html', context)

def paint_dash(request):
    art_list = Arttable.objects.filter(arttype="0").all()

    # Pass the data to the template
    context = {
        'art_list': art_list
    }

    return render(request, 'user_dash.html', context)

def sclupture_dash(request):
    art_list = Arttable.objects.filter(arttype="1").all()

    # Pass the data to the template
    context = {
        'art_list': art_list
    }

    return render(request, 'user_dash.html', context)

def doodling_dash(request):
    art_list = Arttable.objects.filter(arttype="3").all()

    # Pass the data to the template
    context = {
        'art_list': art_list
    }

    return render(request, 'user_dash.html', context)
