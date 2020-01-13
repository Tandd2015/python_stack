from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows/new$', views.index1),
    url(r'^shows/create$', views.new_show_add),
    url(r'^shows/(?P<the_show_id>\d+)$', views.new_show_index),
    url(r'^shows$', views.all_show_index),
    url(r'^shows/(?P<the_edit_id>\d+)/edit$', views.edit_show_index),
    url(r'^shows/(?P<the_update_id>\d+)/update$', views.update_show),
    url(r'^shows/(?P<the_destroy_id>\d+)/destroy$', views.destroy_show),
]