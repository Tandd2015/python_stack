from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^clear$', views.function_one),
    url(r'^process$', views.function_two),
    url(r'^process_money$', views.function_three),
]