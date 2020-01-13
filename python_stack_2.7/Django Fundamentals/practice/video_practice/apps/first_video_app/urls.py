from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^index/', views.index, name="index"),
    # url(r'^index/$', views.index, name="index"),
    # url(r'^$', views.index, name="index"),
    url(r'^first_video_app/index/$', views.index, name="index"),
    url(r'^process/$', views.process, name="process"),
]
