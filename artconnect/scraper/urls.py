from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.scrape_events, name="scrape_events"),
]
