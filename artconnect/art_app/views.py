from django.shortcuts import render,redirect
from .models import Artisttable,Arttable,Usertable,Ordertable
from django.core.files.storage import FileSystemStorage
from django.contrib import messages  # Import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt





from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Usertable, Arttable, Ordertable, Artisttable

def art_upload(request):
    id = request.session.get('user_id', 1)  # Default to 1 for testing, use session ID in production
    results = Usertable.objects.filter(id=id)  # Get user details
    details = Artisttable.objects.filter(userid=id)  # Get artist details
    art_list = Arttable.objects.filter(userid=id, status=1)  # Get user art list

    if request.POST:
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        price = request.POST.get("price")
        arttype = request.POST.get("arttype")
        img = request.FILES.get("img")

        if img:
            fs = FileSystemStorage(location="media/art_photos/")
            filename = fs.save(img.name, img)
            file_url = f"art_photos/{filename}"
        else:
            file_url = ""  # Handle case when no image is uploaded

        Art_obj = Arttable(title=title, desc=desc, price=price, img=file_url, userid=id, status=1, arttype=arttype)
        Art_obj.save()
        messages.success(request, "Art uploaded successfully!")  # Success message

    # Fetch orders for the user's products
    user_products = Arttable.objects.filter(userid=id).values_list('id', flat=True)
    orders = Ordertable.objects.filter(product_id__in=user_products)

    order_details = []
    for order in orders:
        try:
            buyer = Usertable.objects.get(id=order.user_id)  # Buyer details
            product = Arttable.objects.get(id=order.product_id)  # Product details

            order_details.append({
                "buyer_name": buyer.name,
                "buyer_email": buyer.email,
                "product_title": product.title,
                "price": product.price,
                "del_date": order.delivery_date,
                "order_id": order.id  # Needed for passing order ID in the button
            })
        except Usertable.DoesNotExist:
            continue  # Skip if buyer does not exist
        except Arttable.DoesNotExist:
            continue  # Skip if product does not exist

    # ✅ Merge `context` properly
    context = {
        'results': results,
        'details': details,
        'art_list': art_list,
        'orders': order_details  # Include orders in the context
    }

    return render(request, 'artist_registered.html', context)




def artist_page(request):
    return render(request,'artist.html')



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

        
        Usertable.objects.filter(id=id).update(status=1)
        Artisttable_obj=Artisttable(bio=bio,phone=phone,location=location,insta=insta,website=website,art_categories=categories_str,profile_photo=file_url,userid=id)
        Artisttable_obj.save()
    return render(request,'artist_dash.html',context)


@csrf_exempt
def update_delivery_date(request, order_id):
    if request.method == "POST":
        new_date = request.POST.get("date_delivery")  # Get date from form
        try:
            order = Ordertable.objects.get(id=order_id)
            order.delivery_date = new_date  # Update delivery date
            order.save()  # Save changes
            return redirect('art_upload')  # Redirect after updating
        except Ordertable.DoesNotExist:
            return HttpResponse("Order not found", status=404)
    return redirect('art_upload')















def artist_dash(request):

    return render(request, 'artist_dash.html')







