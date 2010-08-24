from django.shortcuts import get_object_or_404, render_to_response, _get_queryset
from django.db import transaction
from cmdb.models import *
from cmdb.helpers import *

def cmdb_index(request):
	return render_to_response('cmdb/index.html')

def default_index(request, klass):
	queryset = _get_queryset(globals()[klass])
	default_list = queryset.all()
	return render_to_response('cmdb/default/list.html',
		{ 'list': default_list,
			'type': klass.lower(),
		})

def default_detail(request, klass, default_name):
	queryset = _get_queryset(globals()[klass])
	default = queryset.get(name=default_name)

	attrs = default.__dict__
	return render_to_response('cmdb/default/detail.html',
		{ 'item': default,
			'type': klass.lower(),
			'attributes': attrs,
		})

def system_index(request):
	return system_list(request)

def system_list(request):
	system_list = System.objects.all()
	return render_to_response('cmdb/system/list.html',
		{ 'system_list': system_list, })

def system_detail(request, system_name):
	system = get_object_or_404(System, name=system_name)
	return render_to_response('cmdb/system/detail.html',
		{ 'system': system,
		})

def server_index(request):
	return server_list(request)

def server_list(request):
	server_list = Server.objects.all()
	return render_to_response('cmdb/server/list.html',
		{ 'server_list': server_list,
		})

def server_detail(request, server_name):
	server = get_object_or_404(Server, name=server_name)
	return render_to_response('cmdb/server/detail.html',
		{ 'server': server,
		})

@transaction.commit_on_success
def receive_facts(request):
	from django.http import HttpResponse

	if request.META['REQUEST_METHOD'] != 'POST':
		return HttpResponse('Only POST allowed')
	facts = request.POST

	# facter needs to be run under root
	if facts['id'] != 'root':
		return HttpResponse('Non privilege user')

	# server - continues above
	server = get_object_or_none(Server, name=facts['hostname'])
	if not server:
		server = Server()
		server.name = facts['hostname']

	# physical or virtual
	if facts['is_virtual'] == 'false': # physical
		# manufacturer
		manufacturer = get_object_or_create(Manufacturer, name=facts['manufacturer'])

		# server type
		server_type = get_object_or_create(ServerType, name=facts['productname'],
			manufacturer=manufacturer)

		server.virtual = False
		server.serial = facts['serialnumber']
	else: # virtual
		server.virtual = True
		server_type = get_object_or_create(ServerType, name=facts['virtual'])

	# architecture
	architecture = get_object_or_create(Architecture, name=facts['architecture'])

	# operating system
	operatingsystem = get_object_or_create(OperatingSystem, name=facts['operatingsystem'], version=facts['lsbdistrelease'], architecture=architecture)


	server.memory = normalize_memory(facts['memorysize'])
	server.operating_system = operatingsystem
	server.server_type = server_type
	server.save()

	# network interfaces
	for nic in facts['interfaces'].split(','):
		if facts.has_key('ipaddress_' + nic):
			# find network/create
			network = get_object_or_none(Network,
				network=facts['network_' + nic],
				netmask=facts['netmask_' + nic]
			)
			if not network:
				network = create_network(facts['network_' + nic], facts['netmask_' + nic])
			# find ip address
			# TODO - should not create if network creates all ip address
				ipaddress = get_object_or_create(InternetAddress, address=facts['ipaddress_' + nic],
					network=network)
			# find nic/create
				networkinterface = get_object_or_create(NetworkInterface,
					name=nic, macaddress=facts['macaddress_' + nic],
					ipaddress=ipaddress, server=server)

	return HttpResponse('OK')
