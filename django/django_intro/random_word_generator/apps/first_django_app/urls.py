from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^random_word$', views.index),
    url(r'^random_word_form$', views.function_one),
    url(r'^clear$', views.function_two),
]