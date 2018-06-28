from django.conf.urls import url
from . import views


urlpatterns =[
url(r'^$',views.soccer_list, name='soccer_list'),
url(r'^soccer/(?P<pk>\d+)/$', views.soccer_detail, name='soccer_detail'),
url(r'^soccer/new/$', views.soccer_new, name='soccer_new'),
url(r'^soccer/(?P<pk>\d+)/edit/$', views.soccer_edit, name='soccer_edit'),
url(r'^soccer/(?P<pk>\d+)/remove/$', views.soccer_remove, name='soccer_remove'),
url(r'^soccer/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]