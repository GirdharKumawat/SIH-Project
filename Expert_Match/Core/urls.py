# core -> urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # The root path for the 'home' view
    path('signup',views.signup,name='signup'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('candidates',views.candidates,name='candidates'),
    path('userLogout',views.userLogout,name='userLogout'),
]
