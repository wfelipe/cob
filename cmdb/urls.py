from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^system/$', 'cob.cmdb.views.system_index'),
	(r'^system/(?P<system_name>[^/]+)/$', 'cob.cmdb.views.system_detail'),
	(r'^system/(?P<system_name>[^/]+)/(?P<component_name>[^/]+)/$', 'cob.cmdb.views.system_component'),

	(r'^server/$', 'cob.cmdb.views.server_index'),
	(r'^server/list/$', 'cob.cmdb.views.server_list'),
	(r'^server/(?P<server_name>[^/]+)/$', 'cob.cmdb.views.server_detail'),
)
