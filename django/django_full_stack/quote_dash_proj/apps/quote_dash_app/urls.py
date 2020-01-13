from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.log_reg_index),
    url(r'^success_process_reg$', views.register_submit),
    url(r'^success_process_log$', views.login_submit),
    url(r'^clear$', views.logout),
    url(r'^quotes$', views.success_index),
    url(r'^mad/quoter$', views.quote_submit),
    url(r'^mad/liker/(?P<q_like_id>\d+)$', views.like_submit),
    url(r'^myaccount/(?P<the_edit_id>\d+)', views.edit_user_index),
    url(r'^edit/(?P<the_edit_id>\d+)$', views.edit_user_submit),
    url(r'^delete/(?P<the_delete_id>\d+)', views.delete_quote),
]