from django.urls import path
from . import views

handler404 = views.custom_404

urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('brand-guide', views.brandguide, name='brandguide'),
    path('boba-bar', views.bobabar, name='bobabar'),
    path('campsite-companions', views.campsitecompanions, name='campsitecompanions'),
    path('communications-certificate', views.communicationscertificate, name='communicationscertificate'),
    path('pottery-company-rebrand', views.potterycompanyrebrand, name='potterycompanyrebrand'),
    path('crochet', views.crochet, name='crochet'),
    path('image-sources', views.imagesources, name='imagesources'),
    path('boba-bar-landing-page', views.bobabarlandingpage, name='bobabarlandingpage'),
    path('campsite-companions-landing-page', views.campsitecompanionslandingpage, name='campsitecompanionslandingpage'),
]