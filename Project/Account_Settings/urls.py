from django.urls import path
# from First_App import views

from . import views


urlpatterns = [
    path('', views.account, name='account_settings.html'),
        
]