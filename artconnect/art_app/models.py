from django.db import models

# Create your models here.
class Usertable(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    role=models.CharField(max_length=30)

class Artisttable(models.Model):
    name=models.CharField(max_length=30)
    bio=models.TextField(max_length=100)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    insta=models.CharField(max_length=50)
    website=models.CharField(max_length=60)
    art_cat=models.CharField(max_length=30)
