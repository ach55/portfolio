from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('projects', views.projects),
    path('brand-guide', views.brandguide),
    path('boba-bar', views.bobabar),
    path('campsite-companions', views.campsitecompanions)
]