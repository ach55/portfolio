from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def projects(request):
    return render(request, 'base/projects.html')

def brandguide(request):
    return render(request, 'base/brand-guide.html')

def bobabar(request):
    return render(request, 'base/boba-bar.html')

def campsitecompanions(request):
    return render(request, 'base/campsite-companions.html')