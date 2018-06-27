from django.conf.urls import url
from . import views.soccer_list

url(r'^$',views.soccer_list, name='soccer_list')