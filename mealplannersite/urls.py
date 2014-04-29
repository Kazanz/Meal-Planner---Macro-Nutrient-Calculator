from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^register/', include('users.urls', namespace='register')), #app = users 
	url(r'^food-list/', include('foods_data.urls', namespace='list')), #app = foods_data 
    url(r'^admin/', include(admin.site.urls)),
)