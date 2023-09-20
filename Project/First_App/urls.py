from django.urls import path
# from First_App import views

from . import views


urlpatterns = [
    path('', views.first, name='index'),

    path('login/', views.login, name='login'),
    path('signup/', views.signin, name='signin'),
    path('menu/', views.menulist, name='menu'),
        
]