from django.shortcuts import render,redirect,get_object_or_404
from .models import Listing
from django.core.paginator import Paginator,EmptyPage
# Create your views here.

def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator= Paginator(listings,4)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'listings':page_listings
    }
    return render(request,'Kitmain/product_index.html',context)

def listing(request,pk):
    listing = get_object_or_404(Listing,pk=pk)
    context = {
        'listing' : listing
    }
    return render(request,'listings/listing.html',context)

def search(request):
    query_set = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set = query_set.filter(description__icontains=keywords)
    context = {
        'query_set':query_set
    }
    return render(request,'listings/search.html',context)
