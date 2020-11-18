from django.urls import path, re_path
from .views import index, search, locations,location_zones

urlpatterns = [
    path('', index, name = 'index' ),
    path('search/', search, name ='search'),
    path('locations/',location_zones, name='location'),
    path('location/<location>',locations, name = 'locations')

]