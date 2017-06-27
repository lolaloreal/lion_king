from django.conf.urls import url
from . import views

app_name = 'python_exam'
urlpatterns = [
    url(r'^$', views.index, name ="index"),
    url(r'^travel$', views.travel, name ="travel"),
    url(r'^travel_add$', views.travel_add, name ="travel_add"),
    url(r'^logout$', views.logout, name ="logout"),
    url(r'^add$', views.add, name ="add"),
    url(r'^destination$', views.destination, name="destination"),
    url(r'^destination/(?P<trip_id>\d+)/$', views.destination_place, name='destination_place'),
]
