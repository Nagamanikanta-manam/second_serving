from django.contrib import admin
from django.urls import path,include
from .views import *
# urls.py
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('a/',home,name='home'),
    path('register/',create_user),

    path('login/',login_c,name='login'),
    path('logout/',log_out,name="logout"),
    path('add_food/',add_food,name="add_food"),
    path('bio_login/',bio_login,name="bio_login")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)