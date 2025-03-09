from django.shortcuts import render,get_object_or_404,redirect,reverse
from art_app.models import Arttable,Usertable,Artisttable,Ordertable,reviewtable

from django.http import JsonResponse
from django.template.loader import render_to_string

import secrets



# Create your views here.

def user_dash(request):
    art_list = Arttable.objects.all()

    # Pass the data to the template
    context = {
        'art_list': art_list
    }

    return render(request, 'user_dash.html', context)

def digital_dash(request):
    art_list = Arttable.objects.filter(arttype="2").all()

    # Pass the data to the template
    context = {
        'art_list': art_list
    }

    return render(request, 'user_dash.html', context)

def paint_dash(request):
    art_list = Arttable.objects.filter(arttype="0").all()

    # Pass the data to the template
    context = {
        'art_list': art_list
    }

    return render(request, 'user_dash.html', context)

def sclupture_dash(request):
    art_list = Arttable.objects.filter(arttype="1").all()

    # Pass the data to the template
    context = {
        'art_list': art_list
    }

    return render(request, 'user_dash.html', context)

def doodling_dash(request):
    art_list = Arttable.objects.filter(arttype="3").all()

    # Pass the data to the template
    context = {
        'art_list': art_list
    }

    return render(request, 'user_dash.html', context)


def details_page(request,id):
    art = get_object_or_404(Arttable, id=id)  # Fetch the art object by ID

    user_id=art.userid

    user_artist = get_object_or_404(Usertable, id=user_id)  # Fetch the art object by ID


    return render(request, 'detail.html', {'art': art,'user_artist':user_artist})



def artist_profile_page(request,id):
        
    user_artist = get_object_or_404(Usertable, id=id)  # Fetch the art object by ID

    us_id=user_artist.id

    artist_details=get_object_or_404(Artisttable,userid=id)

    artist_details_art = Arttable.objects.filter(userid=id)  # Fetch multiple objects


    return render(request,'artist_profile.html',{'user_artist':user_artist,'artist_details':artist_details,'artist_details_art':artist_details_art})

def search(request):
    price_filter = request.GET.get('price') 

    if(price_filter=='1'):
        art_list=Arttable.objects.filter(price__lt=100)
    elif(price_filter=='2'):
        art_list=Arttable.objects.filter(price__gte=100,price__lte=1000)
    elif(price_filter=='3'):
        art_list=Arttable.objects.filter(price__gte=1000)
    else:
        art_list=Arttable.objects.all()



    context = {
        'art_list': art_list,
        'price_filter':price_filter
    }
    return render(request, 'user_dash.html',context)



def live_search(request):
    query = request.GET.get('query', '').strip()
    print(query)
    if query:
        art_list = Arttable.objects.filter(title__icontains=query)
    else:
        art_list = Arttable.objects.all()

    # Render the search results to a separate HTML snippet
    html = render_to_string('search_results.html', {'art_list': art_list})
    return JsonResponse(html, safe=False)


def paymentpage(request,id):
    art = get_object_or_404(Arttable, id=id)
    return render(request, 'payment-form.html',{'art': art})



def process_payment(request):
    if request.method == 'POST':
        try:
            # Just log the data received without trying to save anything
            print("Received data:", dict(request.POST))
            print("Session data:", dict(request.session))

            Ordertable_obj = Ordertable(
                   payment_id=secrets.token_hex(4),
                   product_id=request.POST.get('product_id'),
                   user_id=request.session.get('user_id'),
                   delivery_address=request.POST.get('address'),
                   delivery_status=0
                )
            Ordertable_obj.save()
            
            # Return success without doing anything database-related
            return JsonResponse({
                'status': 'success',
                'redirect_url': reverse('user_dashboard')
            })
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error'}, status=405)

def myorders(request):
    user_id=request.session.get('user_id')

    orderdetails=Ordertable.objects.filter(user_id=user_id)

    product_ids = orderdetails.values_list('product_id', flat=True)

    products = Arttable.objects.filter(id__in=product_ids)

    zip_items = zip(products, orderdetails)
    
    context = {
        'art_list': products,
        'orderdetails': orderdetails,
        'zip_items': zip_items,
    }



    return render(request,'user_dash_orders.html',context)

def reviewpage(request,id):
    if request.method == 'POST':
        reviewtable_obj = reviewtable(
                   userid=request.session.get('user_id'),
                   product_id=id,
                   rev_title=request.POST.get('reviewTitle'),
                   rev_body=request.POST.get('reviewContent'),
                   rating=request.POST.get('rating')
                )
        reviewtable_obj.save()
        return redirect('details',id=id)
            
      

    return render(request,'review.html')