from django.conf.urls import url
from find import views


urlpatterns = [
    url(r'^$', views.index_page, name='index'),
]
