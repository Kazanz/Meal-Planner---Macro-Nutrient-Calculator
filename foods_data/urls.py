from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from foods_data import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='list'),
    url(r'^add/$', views.add, name='add'),
    url(r'^remove/$', views.remove, name='remove'),
)
