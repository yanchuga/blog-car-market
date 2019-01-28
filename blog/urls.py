from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.cars_list, name='cars_list'),
    url(r'^car/(?P<pk>\d+)/$', views.car_detail, name='car_detail'),
    url(r'^car/new/$', views.car_new, name='car_new'),
    url(r'^car/del/(?P<pk>\d+)/$', views.car_del, name='car_del'),
    url(r'^car/(?P<pk>\d+)/edit/$', views.car_edit, name='car_edit'),
]
