# Expert_match .py
from django.contrib import admin
from django.urls import path ,include
import Core.urls
import Core.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(Core.urls))
]
