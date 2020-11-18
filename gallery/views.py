from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Image, Location, Category

# Create your views here.

def index(request):
    title = 'Welcome to MyLouvre'
    images = Image.objects.all()

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        search_name=f"/search/?search_term={search_term}"

        return redirect (search_name)
    else:

        return render(request, 'index.html', {"title":title, "images":images})

def search(request):
    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_image = Image.search_image("search_term")
        if searched_image != "No Image Found":
            message = "Photos of '" + search_term + "'"
            return render(request, "search.html", {"images":searched_image, "message":message,"title":search_term})
        else:
            message = "No images found"
            return render(request, "search.html",{"images":[],"message":message,"title":search_term})
            
def location_zones(request):
    return render(request,"locations.html",{"title":locations})

def locations(request,location):

    photos = Image.filter_by_location(location)
    
    return render (request,"location.html",{"images":photos, "title":location})