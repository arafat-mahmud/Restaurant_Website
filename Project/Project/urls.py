# Project/urls.py


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('First_App.urls')),
    path('as/', include('Account_Settings.urls')),
]
