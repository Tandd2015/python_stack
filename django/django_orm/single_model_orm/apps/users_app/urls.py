from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users_app$', views.index),
]