from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'cmdb.views.cmdb_index'),
	# generic list and detail
	(r'^manufacturer/$', 'cmdb.views.default_index', { 'klass': 'Manufacturer' }),
	(r'^manufacturer/(?P<default_name>[^/]+)/$', 'cmdb.views.default_detail', { 'klass': 'Manufacturer' }),
	(r'^architecture/$', 'cmdb.views.default_index', { 'klass': 'Architecture' }),
	(r'^architecture/(?P<default_name>[^/]+)/$', 'cmdb.views.default_detail', { 'klass': 'Architecture' }),
	(r'^operatingsystem/$', 'cmdb.views.default_index', { 'klass': 'OperatingSystem' }),
	(r'^operatingsystem/(?P<default_name>[^/]+)/$', 'cmdb.views.default_detail', { 'klass': 'OperatingSystem' }),
	(r'^network/$', 'cmdb.views.default_index', { 'klass': 'Network' }),
	(r'^network/(?P<default_name>[^/]+)/$', 'cmdb.views.default_detail', { 'klass': 'Network' }),
	(r'^internetaddress/$', 'cmdb.views.default_index', { 'klass': 'InternetAddress' }),
	(r'^internetaddress/(?P<default_name>[^/]+)/$', 'cmdb.views.default_detail', { 'klass': 'InternetAddress' }),
	(r'^networkinterface/$', 'cmdb.views.default_index', { 'klass': 'NetworkInterface' }),
	(r'^networkinterface/(?P<default_name>[^/]+)/$', 'cmdb.views.default_detail', { 'klass': 'NetworkInterface' }),
	(r'^servertype/$', 'cmdb.views.default_index', { 'klass': 'ServerType' }),
	(r'^servertype/(?P<default_name>[^/]+)/$', 'cmdb.views.default_detail', { 'klass': 'ServerType' }),

	(r'^system/$', 'cmdb.views.system_index'),
	(r'^system/(?P<system_name>[^/]+)/$', 'cmdb.views.system_detail'),
	(r'^system/(?P<system_name>[^/]+)/(?P<component_name>[^/]+)/$', 'cmdb.views.system_component'),

	(r'^server/$', 'cmdb.views.server_index'),
	(r'^server/list/$', 'cmdb.views.server_list'),
	(r'^server/facts/$', 'cmdb.views.receive_facts'),
	(r'^server/(?P<server_name>[^/]+)/$', 'cmdb.views.server_detail'),
)
