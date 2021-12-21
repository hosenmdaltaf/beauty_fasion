from django.shortcuts import render,get_object_or_404
from servicepage.models import Service,Category
from homepage.models import Review, Team


def service(request):
    services = Service.objects.all()
    return render(request,'servicepage/service.html',{'services':services})

def team(request):
    teams = Team.objects.all()
    return render(request,'servicepage/team.html',{'teams':teams})


def service_details(request,pk):
    object = Service.objects.get(pk=pk)
    category = Category.objects.all()
    return render(request,'servicepage/service_details.html',{'object':object,'category':category})


def testimonial(request):
    testimonials = Review.objects.all()
    return render(request,'servicepage/testimonial.html',{'testimonials':testimonials})


def category_details(request,pk):
    category_service = Service.objects.filter(service=pk)
    return render(request,'servicepage/category_details.html',{'category_service':category_service})