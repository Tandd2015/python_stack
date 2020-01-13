from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main$', views.main_page_index_template),
    url(r'^success$', views.register_success_test),
    url(r'^dashboard$', views.dashboard_index_template),
    url(r'^clear$', views.logout),
    url(r'^login_success$', views.login_success_test),
    url(r'^wish_items/create', views.wish_items_index_template),
    url(r'^created_success$', views.item_create_success_test),
    url(r'^item_delete_success/(?P<the_delete_id>\d+)$', views.item_delete_success_test),
    url(r'^item_show_success/(?P<the_show_id>\d+)$', views.item_show_index_template),
    url(r'^item_add_success/(?P<the_add_id>\d+)$', views.item_add_success),
]