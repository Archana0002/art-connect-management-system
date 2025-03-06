from django.shortcuts import render
from .models import Artisttable,Arttable,Usertable
from django.core.files.storage import FileSystemStorage
from django.contrib import messages  # Import messages




def art_upload(request):
    id = request.session.get('user_id',1)  # Default to 7 for testing, use session ID in production
    results = Usertable.objects.filter(id=id)  # Get user details
    details = Artisttable.objects.filter(userid=id)  # Get user details
    art_list = Arttable.objects.filter(userid=id,status=1)  # Get user details

    context = {
        'results': results ,
        'details':details, # Pass queryset to the template
        'art_list':art_list
    }
    if request.POST:
        title=request.POST.get("title")
        desc=request.POST.get("desc")
        price=request.POST.get("price")
        arttype=request.POST.get("arttype")
        img=request.FILES.get("img")
        fs = FileSystemStorage(location="media/art_photos/")
        filename = fs.save(img.name, img)
        file_url = f"art_photos/{filename}"
        Art_obj=Arttable(title=title,desc=desc,price=price,img=file_url,userid=id,status=1,arttype=arttype)
        Art_obj.save()
        messages.success(request, "Art uploaded successfully!")  # Success message


    return render(request,'artist_registered.html',context)

def details_page(request):
    return render(request,'detail.html')

def artist_page(request):
    return render(request,'artist.html')

def artist_profile_page(request):
    return render(request,'artist_profile.html')

def artist_reg(request):
    id = request.session.get('user_id')  # Default to 7 for testing, use session ID in production
    results = Usertable.objects.filter(id=id)  # Get user details

    context = {
        'results': results  # Pass queryset to the template
    }

  


    if request.POST and request.FILES.get("profile_photo"):
        bio=request.POST.get("bio")
        phone=request.POST.get("phone")
        location=request.POST.get("location")
        insta=request.POST.get("insta")
        website=request.POST.get("website")

        selected_categories = request.POST.getlist('art_cat')  # Get selected checkboxes
        categories_str = ",".join(selected_categories)

        profile_photo = request.FILES["profile_photo"]
        fs = FileSystemStorage(location="media/profile_photos/")
        filename = fs.save(profile_photo.name, profile_photo)
        file_url = f"profile_photos/{filename}"  # Relative path for the database

        

        Artisttable_obj=Artisttable(bio=bio,phone=phone,location=location,insta=insta,website=website,art_categories=categories_str,profile_photo=file_url,userid=id)
        Artisttable_obj.save()
    return render(request,'artist_dash.html',context)


















def artist_dash(request):

    return render(request, 'artist_dash.html')







