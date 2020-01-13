from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout$', views.checkout_index),
    url(r'^amadon/buy$', views.amadon_buying),
]