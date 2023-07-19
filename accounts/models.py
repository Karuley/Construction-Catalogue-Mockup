from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name"""


class Company(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    logo = models.ImageField(default='defaulticon.jpg', upload_to='gallery/', blank=True, null = True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name != None:
            return self.name
        else:
            return 'No name'
    
class Tags(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name


class Catalogue(models.Model):
    
    def __str__(self):
            return self.name

class Products(models.Model):
    CATEGORY = (
            ('Interior', 'Interior'),
            ('Exterior', 'Exterior'),
            )

    image = models.ImageField(upload_to='images/',blank=False, null = True)
    company = models.ForeignKey(Company, null=True, on_delete= models.SET_NULL)
    tags = models.ManyToManyField(Tags)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



