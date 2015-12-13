from django.conf.urls import include, url
from find import views
urlpatterns = [
    url(r'^$', include('find.urls', namespace="find")),
    url(r'^food\/(?P<location>/*.+)$',
        views.get_food, name='restaurant'),
    url(r'^cafe\/(?P<location>/*.+)$',
        views.get_cafes, name='cafe'),
    url(r'^dessert\/(?P<location>/*.+)$',
        views.get_desserts, name='dessert'),
    url(r'^wronglocation$',
        views.wrong_location, name='wrong_location'),


]
