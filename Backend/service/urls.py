from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^stations', views.list_stations, name='station_list'),
    url(r'^trains', views.get_train_list, name='train_list'),
    url('routemap', views.get_train_route_map, name='route_map'),
    url(r'^delay', views.get_train_delay, name='delay'),
    url(r'^explain', views.get_delay_explanation, name='explain'),
    url('htmlroute', views.get_train_route_map_html_file, name='routemaphtmlview'),
    url('limehtml', views.get_delay_explanation_filepath, name='limehtmlview')
]
