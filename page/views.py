from django.shortcuts import render
from django.http  import HttpResponse
from listings.models import Listing
# Create your views here.
def about(request):
    return render(request,"page/about.html")
def dashboard(request):
    return render(request,"page/dashboard.html")
def index(request):
    latest_listings=Listing.objects.all()
    context={
    'latest_listings':latest_listings
    }
    return render(request,"page/index.html",context)
def login(request):
    return render(request,"page/login.html")
def register(request):
    return render(request,"page/register.html")
def search(request):
    return render(request,"page/search.html")
