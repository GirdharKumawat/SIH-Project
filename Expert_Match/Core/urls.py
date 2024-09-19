# core -> urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # The root path for the 'home' view
    path('signup',views.signup,name='signup'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('candidates',views.candidates,name='candidates'),
    path('expert',views.expert,name='expert'),
    path('add_expert/', views.add_expert, name='add_expert'),
    path('add_candidate/', views.add_candidate, name='add_candidate'),
    path('match/<int:pk>',views.match,name='match'),
    path('userLogout',views.userLogout,name='userLogout'),
]
