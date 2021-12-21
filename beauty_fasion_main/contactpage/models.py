from django.db import models

# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(max_length=30,null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    message = models.TextField(max_length=300,null=True,blank=True)

    def __str__(self):
        return str(self.name)

