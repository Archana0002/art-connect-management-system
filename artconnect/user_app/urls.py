from django.urls import path
from . import views 

urlpatterns = [
    path('user_dash',views.user_dash,name='user_dashboard'),
]