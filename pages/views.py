from django.shortcuts import render
from .models import Team
from flats.models import Flat  # Import Flat model from flats app
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured = Flat.objects.order_by('-created_date').filter(is_featured=True)
    all_listings = Flat.objects.order_by('-created_date')
    types = Flat.objects.values_list('type', flat=True).distinct()
    rents_sales = Flat.objects.values_list('rent_sale', flat=True).distinct()
    cities = Flat.objects.values_list('city', flat=True).distinct()
    bedrooms = Flat.objects.values_list('bedrooms', flat=True).distinct()

    teams_data ={
        'teams': teams,
        'featured': featured,
        'all_listings': all_listings,
        'types': types,
        'rents_sales': rents_sales,
        'cities': cities,
        'bedrooms': bedrooms,
    }
    return render(request, 'pages/home.html', teams_data)

def about(request):
    teams = Team.objects.all()
    teams_data ={
        'teams': teams,
    }
    return render(request, 'pages/about.html', teams_data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        message_body =  'Name: '+ first_name + ', Email:'+ email +  ', Message:' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email 
                    #send_mail(
                        #"New Inquiry",
                        # message_body,
                        #from email:
                        #"example_from_email@gmail.com",
                        # to email - superuser email:
                        #[admin_email],
                        #fail_silently=False,
                    #)
        messages.success(request, 'Thank you, we will get back to you shortly')

    return render(request, 'pages/contact.html')

def base(request):
    return render(request, 'base.html')