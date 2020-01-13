from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.log_reg_index),
    url(r'^success_process_reg$', views.register_submit),
    url(r'^success_process_log$', views.login_submit),
    url(r'^clear$', views.logout),
    url(r'^success$', views.success_index),

]