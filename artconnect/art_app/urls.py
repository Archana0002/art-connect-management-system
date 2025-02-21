from django.urls import path
from . import views 

urlpatterns = [
    path("details",views.details_page,name="details"),
    path("artist",views.artist_page,name="artist"),
    path("artist_profile",views.artist_profile_page,name="artist_profile"),
    path("art_upload",views.art_upload,name="art_upload")
]