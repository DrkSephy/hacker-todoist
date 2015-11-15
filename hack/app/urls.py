# app/urls.py

from django.conf.urls import url

from app import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test/$', views.test, name='test'),
  url(r'^events/$', views.events, name='events'),
  url(r'^fetchDatabase/$', views.fetchDatabase, name='fetchDatabase'),
  url(r'^fetchNumbers/$', views.fetchNumbers, name='fetchNumbers'),
  url(r'^clearDatabases/$', views.clearDatabases, name='clearDatabases'),
  url(r'^fetchBitbucketDatabase/$', views.fetchBitbucketDatabase, name='fetchBitbucketDatabase'),

]
