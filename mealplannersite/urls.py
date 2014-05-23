from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^food-list/', include('foods_data.urls', namespace='list')), #app = foods_data 
        url(r'^admin/', include(admin.site.urls)),
)
