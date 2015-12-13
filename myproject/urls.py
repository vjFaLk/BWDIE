"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from find import views
urlpatterns = [
    url(r'^$', include('find.urls', namespace="find")),
    url(r'^food\/(?P<location>/*.+)$',
        views.get_food, name='restaurant'),
    url(r'^cafe\/(?P<location>/*.+)$',
        views.get_cafes, name='cafe'),
    url(r'^drink\/(?P<location>/*.+)$',
        views.get_drinks, name='drink'),
    url(r'^dessert\/(?P<location>/*.+)$',
        views.get_desserts, name='dessert'),
    url(r'^wronglocation$',
        views.wrong_location, name='wrong_location'),


]
