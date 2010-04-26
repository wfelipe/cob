from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^domains/$', 'cob.dns.views.domain_list'),
    (r'^domains/(?P<domain_id>\d+)/$', 'cob.dns.views.domain_detail'),
    (r'^domains/compare/?$', 'cob.dns.views.domain_compare'),
    (r'^domains/new/?$', 'cob.dns.views.domain_new'),
)
