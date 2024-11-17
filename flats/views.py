from django.shortcuts import render, get_object_or_404
from flats.models import Flat  # Import Flat model from flats app
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def flats(request):
    flats = Flat.objects.order_by('-created_date')
    paginator = Paginator(flats, 4)
    page = request.GET.get('page')
    paged_flats = paginator.get_page(page)
    
    types = Flat.objects.values_list('type', flat=True).distinct()
    rents_sales = Flat.objects.values_list('rent_sale', flat=True).distinct()
    cities = Flat.objects.values_list('city', flat=True).distinct()
    bedrooms = Flat.objects.values_list('bedrooms', flat=True).distinct()

    data = {
        'flats': paged_flats,
        'types': types,
        'rents_sales': rents_sales,
        'cities': cities,
        'bedrooms': bedrooms,
    }
    return render(request, 'flats/flats.html', data)

    
def flat_detail(request, id):
    listing = get_object_or_404(Flat, pk=id)
    data = {
        'listing': listing,
    }

    return render(request, 'flats/flat_detail.html', data)

def search(request):
    listings = Flat.objects.order_by('-created_date')
    #search functionality: if keyword typed (appears in URL), if not blank check if its in 
    #one of the listings' description. if yes then update the data to that
    types = Flat.objects.values_list('type', flat=True).distinct()
    rents_sales = Flat.objects.values_list('rent_sale', flat=True).distinct()
    cities = Flat.objects.values_list('city', flat=True).distinct()
    bedrooms = Flat.objects.values_list('bedrooms', flat=True).distinct()
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            listings = listings.filter(description__icontains=keyword)
            
    if 'type' in request.GET:
        type = request.GET['type']
        if type:
            listings = listings.filter(type__iexact=type)
            
    if 'rent_sale' in request.GET:
        rent_sale = request.GET['rent_sale']
        if rent_sale:
            listings = listings.filter(rent_sale__iexact=rent_sale)
            
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)
            
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__iexact=bedrooms)
            
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            listings = listings.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'listings': listings,
        'types': types,
        'rents_sales': rents_sales,
        'cities': cities,
        'bedrooms': bedrooms,
    }
    return render(request, 'flats/search.html', data)    