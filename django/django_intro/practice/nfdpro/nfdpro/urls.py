"""nfdpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include	                # added an import!
# from django.contrib import admin                          # comment out, or just delete
urlpatterns = [
    url(r'^', include('apps.nfdaro.urls')),	                # use your app_name here
    url(r'^', include('apps.nsdaro.urls')),                 # use your app_name here
    url(r'^', include('apps.new_third_django_app.urls')),   # use your app_name here
    url(r'^', include('apps.new_fourth_django_app.urls')),  # use your app_name here
    url(r'^', include('apps.new_fifth_django_app.urls')), # use your app_name here
    url(r'^six/', include('apps.new_sixth_django_app.urls', namespace='new_six')),   # use your app_name here
    # url(r'^admin/', admin.sites.urls)                     # comment out, or just delete
]