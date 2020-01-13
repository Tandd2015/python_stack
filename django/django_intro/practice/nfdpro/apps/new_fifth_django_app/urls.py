from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^session$', views.index),
    url(r'^sessions_form/$', views.some_function),
]
