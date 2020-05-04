from django.shortcuts import render,get_object_or_404
from django.http  import HttpResponse
from .models import Listing
# Create your views here.

def listing(request,id):
    listing=get_object_or_404(Listing,pk=id)
    context={
    'listing':listing
    }
    return render(request,"listings/listing.html",context)
def listings(request):
    listings=Listing.objects.all()
    return render(request,"listings/listings.html")
