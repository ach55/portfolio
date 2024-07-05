from django.urls import path
from . import views

handler404 = views.custom_404

urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('brand-guide', views.brandguide, name='brandguide'),
    path('boba-bar', views.bobabar, name='bobabar'),
    path('campsite-companions', views.campsitecompanions, name='campsitecompanions')
]