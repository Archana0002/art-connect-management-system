from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('artist_dash',views.artist_reg,name='artist_dashboard'),
    path("artist",views.artist_page,name="artist"),
    path("art_upload",views.art_upload,name="art_upload"),
    path('update_delivery/<int:order_id>/', views.update_delivery_date, name='update_delivery_date'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
