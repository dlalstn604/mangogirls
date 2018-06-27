from django.conf.urls import url
from . import views


urlpatterns =[

url(r'^$',views.soccer_list, name='soccer_list'),
 ]