from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('artist_dash',views.artist_reg,name='artist_dashboard'),
    path("details",views.details_page,name="details"),
    path("artist",views.artist_page,name="artist"),
    path("artist_profile",views.artist_profile_page,name="artist_profile"),
    path("art_upload",views.art_upload,name="art_upload")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
