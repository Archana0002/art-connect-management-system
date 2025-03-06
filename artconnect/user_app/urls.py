from django.urls import path
from . import views 

urlpatterns = [
    path('user_dash',views.user_dash,name='user_dashboard'),
    path('digital',views.digital_dash,name='digital_dashboard'),
    path('painting',views.paint_dash,name='paint_dashboard'),
    path('sclupture',views.sclupture_dash,name='sclupture_dashboard'),
    path('doodling',views.doodling_dash,name='doodling_dashboard'),


]