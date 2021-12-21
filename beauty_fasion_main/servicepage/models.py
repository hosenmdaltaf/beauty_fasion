from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Service(models.Model):
    name = models.CharField(max_length=200)
    service=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='service_img',null=True,blank=True)
    details = models.TextField(null=True,blank=True)
    # cost = models.IntegerField()

    def __str__(self):
        return str(self.name)


