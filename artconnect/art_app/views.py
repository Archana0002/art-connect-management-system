from django.shortcuts import render, redirect
from . models import Usertable,Artisttable,Arttable
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage



def art_upload(request):
    if request.POST:
        title=request.POST.get("title")
        desc=request.POST.get("desc")
        price=request.POST.get("price")
        img=request.FILES.get("img")
        fs = FileSystemStorage(location="media/art_photos/")
        filename = fs.save(img.name, img)
        file_url = f"art_photos/{filename}"
        Art_obj=Arttable(title=title,desc=desc,price=price,img=file_url)
        Art_obj.save()

    return render(request,'artist_registered.html')

def details_page(request):
    return render(request,'detail.html')

def artist_page(request):
    return render(request,'artist.html')

def artist_profile_page(request):
    return render(request,'artist_profile.html')

def artist_reg(request):
    if request.POST and request.FILES.get("profile_photo"):
        name=request.POST.get("name")
        bio=request.POST.get("bio")
        email=request.POST.get("email")
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

        

        Artisttable_obj=Artisttable(name=name,bio=bio,email=email,phone=phone,location=location,insta=insta,website=website,art_categories=categories_str,profile_photo=file_url)
        Artisttable_obj.save()
    return render(request,'artist_dash.html')


















def homepage(request):
    return render(request, 'home.html')

def register(request):
    if request.POST:
        if "register_submit" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('opassword')
            cpassword = request.POST.get('cpassword')
            role = request.POST.get('role')

            # Input validation
            try:
                # Validate email format
                validate_email(email)
                
                # Validate password length and complexity
                if len(password) < 8:
                    messages.error(request, "Password must be at least 8 characters long", extra_tags='danger')
                    return redirect('register_page')

                # Check password confirmation
                if cpassword != password:
                    messages.error(request, "Passwords do not match!", extra_tags='danger')
                    return redirect('register_page')

                # Check if user already exists
                if Usertable.objects.filter(email=email).exists():
                    messages.error(request, "An account with this email already exists", extra_tags='warning')
                    return redirect('register_page')

                # Create new user with encrypted password
                hashed_password = make_password(password)
                Usertable_obj = Usertable(
                    name=name,
                    email=email,
                    password=hashed_password,
                    role=role
                )
                Usertable_obj.save()
                
                messages.success(request, "Registration successful! Please login to continue", extra_tags='success')
                return redirect('register_page')

            except ValidationError:
                messages.error(request, "Please enter a valid email address", extra_tags='danger')
                return redirect('register_page')

        elif "login_submit" in request.POST:
            email = request.POST.get("email")
            password = request.POST.get("password")

            try:
                user = Usertable.objects.get(email=email)
                
                # Verify password using check_password
                if check_password(password, user.password):
                    # Set user session
                    request.session['user_id'] = user.id
                    request.session['user_role'] = user.role
                    request.session['user_name'] = user.name

                    role_names = {
                        '0': 'User',
                        '1': 'Artist'
                    }
                    
                    messages.success(
                        request, 
                        f"Welcome back, {user.name}! You're logged in as {role_names.get(user.role, 'Unknown')}", 
                        extra_tags='success'
                    )

                    if user.role == '0':
                        return redirect("user_dashboard")
                    elif user.role == '1':
                        return redirect("artist_dashboard")
                else:
                    messages.error(request, "Invalid password. Please try again.", extra_tags='danger')
            except Usertable.DoesNotExist:
                messages.error(request, "No account found with this email.", extra_tags='danger')
            
            return redirect('register_page')

    return render(request, 'register.html')

def user_dash(request):
    # Check if user is logged in
    if not request.session.get('user_id'):
        messages.error(request, "Please login to access the dashboard", extra_tags='danger')
        return redirect('register_page')
    return render(request, 'user_dash.html')

def artist_dash(request):
    # Check if user is logged in and is an artist
    if not request.session.get('user_id'):
        messages.error(request, "Please login to access the dashboard", extra_tags='danger')
        return redirect('register_page')
    if request.session.get('user_role') != '1':
        messages.error(request, "You don't have permission to access the artist dashboard", extra_tags='danger')
        return redirect('register_page')
    return render(request, 'artist_dash.html')







