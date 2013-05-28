from django.conf.urls import patterns, url

urlpatterns = patterns('analytics.views',
	url(r'^tap/$', 'tap'),
	url(r'^update/$', 'update'),
	url(r'^slide/$', 'slide'),
	url(r'^map_operation/$', 'map_operation'),
	url(r'^open_phone/(?P<device_id>[a-zA-Z0-9]+)/$', 'open_phone'),
	url(r'^close_phone/(?P<device_id>[a-zA-Z0-9]+)/$', 'close_phone'),
	url(r'^tap_phone/(?P<device_id>[a-zA-Z0-9]+)/$', 'tap_phone'),
)