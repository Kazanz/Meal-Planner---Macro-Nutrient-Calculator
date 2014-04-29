from django.conf.urls import patterns, include, url
from users import views

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^$', views.add_new_user, name='add_new_user'),
    url(r'^adding/$', views.adding, name = 'adding'),
)
