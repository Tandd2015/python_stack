from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add_books),
    url(r'^books/(?P<bookin_id>\d+)$', views.view_book),
    url(r'^books/(?P<bookin_id>\d+)/new$', views.view_book_add),
    url(r'^i$', views.index2),
    url(r'^i/add2$', views.add_authors),
    url(r'^i/authors/(?P<author_in_id>\d+)$', views.view_author),
    url(r'^i/authors/(?P<author_in_id>\d+)/new$', views.view_author_add),
]