from django.shortcuts import render
from contactpage.models import Contact

def contact(request):
    # gallerys = Gallery.objects.all()
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Contact.objects.create(name=name,message=message,phone=phone,subject=subject,email=email)
        return render(request,'global/thankyou.html')
    return render(request,'contactpage/contact.html')
