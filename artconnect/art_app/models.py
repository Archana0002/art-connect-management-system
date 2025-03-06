from django.db import models

# Create your models here.
class Usertable(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    status=models.CharField(max_length=30)


class Arttable(models.Model):
    title=models.CharField(max_length=30)
    userid=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    desc=models.CharField(max_length=80)
    price=models.CharField(max_length=20)
    arttype=models.CharField(max_length=20)
    img=models.ImageField(upload_to='art_photos/',blank=True,null=True)


class Artisttable(models.Model):
    userid=models.TextField(max_length=10)
    bio=models.TextField(max_length=100)
    phone=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    insta=models.CharField(max_length=50)
    website=models.CharField(max_length=60)
    ART_CATEGORIES = [
        ('digital', 'Digital Art'),
        ('painting', 'Painting'),
        ('sculpture', 'Sculpture'),
    ]
    

    art_categories = models.CharField(max_length=255,default="")  # Store selected categories as comma-separated values
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)


  
