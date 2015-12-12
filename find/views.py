from django.shortcuts import render
from find.services import *
# Create your views here.


def showHome(request):
    return render(request, 'find/index.html')


def getRestaurants(request, location):
    coordinates = location.split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    restaurants_list = get_restaurants(latitude, longitude, '', '')
    return render(request, 'find/restaurants.html', {'restaurants_list': restaurants_list,
                                                     'lat': latitude,
                                                     'longi': longitude})


def getCafe(request, location):
    coordinates = location.split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    cafe_id = 1 
    cafe_list = get_restaurants(latitude, longitude, '', cafe_id)
    return render(request, 'find/cafe.html', {'cafe_list': cafe_list,
                                              'lat': latitude,
                                              'longi': longitude})


def getDrinks(request, location):
    coordinates = location.split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    drinks_id = 5
    drinks_list = get_restaurants(latitude, longitude, '', drinks_id)
    return render(request, 'find/specific_cuisine.html', {'drinks_list': drinks_list,
                                                          'lat': latitude,
                                                          'longi': longitude})


def getDesserts(request, location):
    coordinates = location.split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    desserts_id = 100
    desserts_list = get_restaurants(latitude, longitude, desserts_id, '')
    return render(request, 'find/desserts.html', {'desserts_list': desserts_list,
                                                  'lat': latitude,
                                                  'longi': longitude})


def wrongLocation(request):
    return render(request, 'find/wrongLocation.html')
