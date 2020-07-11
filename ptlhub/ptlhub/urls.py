from django.contrib import admin
from django.urls import path, include
import allauth

urlpatterns = [
    path('', include('main.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
