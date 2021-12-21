from django.db import models

class Gallery(models.Model):
    image=models.ImageField(upload_to='gallery_img', blank=True, null=True)
    # title=models.CharField( max_length=20, blank=True, null=True)
    # text=models.CharField(max_length=50, blank=True, null=True)


class Review(models.Model):
    image=models.ImageField(upload_to='review_img', blank=True, null=True)
    name=models.CharField(max_length=80, blank=True, null=True)
    text=models.TextField( blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Team(models.Model):
    image=models.ImageField(upload_to='team_img', blank=True, null=True)
    Specialist =models.CharField(max_length=80, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.name)
