from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^some$', views.index),
    url(r'^some_route$', views.some_function),
]
