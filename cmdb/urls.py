from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'cmdb.views.cmdb_index'),
	(r'^manufacturer/$', 'cmdb.views.manufacturer_index'),
	(r'^manufacturer/(?P<manufacturer_name>[^/]+)/$', 'cmdb.views.manufacturer_detail'),
	(r'^system/$', 'cmdb.views.system_index'),
	(r'^system/(?P<system_name>[^/]+)/$', 'cmdb.views.system_detail'),
	(r'^system/(?P<system_name>[^/]+)/(?P<component_name>[^/]+)/$', 'cmdb.views.system_component'),

	(r'^server/$', 'cmdb.views.server_index'),
	(r'^server/list/$', 'cmdb.views.server_list'),
	(r'^server/facts/$', 'cmdb.views.receive_facts'),
	(r'^server/(?P<server_name>[^/]+)/$', 'cmdb.views.server_detail'),
)
