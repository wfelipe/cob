from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'dns.views.domain_list'),
	(r'^domains/$', 'dns.views.domain_list'),
	(r'^domains/(?P<domain_id>\d+)/$', 'dns.views.domain_detail'),
	(r'^domains/compare/?$', 'dns.views.domain_compare'),
	(r'^domains/new/?$', 'dns.views.domain_new'),
)
