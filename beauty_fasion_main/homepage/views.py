from django.shortcuts import render
from homepage.models import Review, Gallery,Team
from servicepage.models import Service

def home(request):
    reviews = Review.objects.all()
    gallerys = Gallery.objects.all()[:3]
    teams = Team.objects.all()[:3]
    services = Service.objects.all()[:2]
    return render(request,'homepage/home.html',{'reviews':reviews,'gallerys':gallerys,'teams':teams,'services':services})

def gallery(request):
    gallerys = Gallery.objects.all()
    return render(request,'servicepage/gallery.html',{'gallerys':gallerys})

