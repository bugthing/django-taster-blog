from django.conf.urls import patterns, include, url
from blog import views
urlpatterns = patterns('',
  url(r'^$', views.list_postings, name='index'),
  url(r'^form/new$', views.show_form),
  url(r'^form/(?P<id>\d+)$', views.show_form),
  url(r'^update/new$', views.update_posting),
  url(r'^update/(?P<id>\d+)$', views.update_posting),
  url(r'^delete/(?P<id>\d+)$', views.delete_posting, name='delete'),
  url(r'^login$', views.log_user_in, name='log_user_in'),
)
