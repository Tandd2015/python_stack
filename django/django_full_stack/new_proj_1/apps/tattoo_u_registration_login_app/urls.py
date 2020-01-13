from django.conf.urls import url
from . import views

urlpatterns = [
    #--- Registration Page Views
    url(r'^registration$', views.registration_index_page_load),
    url(r'^submit_registration_form$',views.registration_form_submit),
    #--- Login Page Views
    url(r'^login$', views.login_index_page_load),
    url(r'^submit_login_form$', views.login_form_submit),
    #--- User Dashboard Views
    url(r'^dashboard', views.user_dashboard_index_page_load),
    url(r'^submit_dashboard_form$', views.user_dashboard_form_submit),
    #--- Nav Bar Redirect Views
    url(r'^nav3/registration/in$', views.registration_redirect),
    url(r'^nav2/logged/in$', views.login_redirect),
    url(r'^nav1/logged/out$', views.logout_redirect),
]