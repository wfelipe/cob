from django.shortcuts import get_object_or_404, render_to_response
from cob.cmdb.models import *

def system_index(request):
	return system_list(request)

def system_list(request):
	system_list = System.objects.all()
	return render_to_response('cmdb/system/system_list.html',
		{ 'system_list': system_list, })

def system_detail(request, system_name):
	system = get_object_or_404(System, name=system_name)
	component_list = Component.objects.filter(system=system)
	return render_to_response('cmdb/system/system_detail.html',
		{ 'system': system,
			'component_list': component_list,
		})

def system_component(request, system_name, component_name):
	system = get_object_or_404(System, name=system_name)
	component = get_object_or_404(Component, name=component_name, system=system)
	return render_to_response('cmdb/system/system_component.html',
		{ 'system': system,
			'component': component,
		})


def server_index(request):
	return server_list(request)

def server_list(request):
	server_list = Server.objects.all()
	return render_to_response('cmdb/server/server_list.html',
		{ 'server_list': server_list,
		})

def server_detail(request, server_name):
	server = get_object_or_404(Server, name=server_name)
	return render_to_response('cmdb/server/server_detail.html',
		{ 'server': server,
		})

def receive_post(request):
	from django.http import HttpResponse

	facts = request.POST

	# facter needs to be run under root
	if facts['id'] != 'root':
		return HttpResponse('Non privilege user')

	# physical or virtual
	if facts.['is_virtual']:
		manufacturer_name = facts['virtual']
	else:
		manufacturer_name = facts['manufacturer']

	# manufacturer
	try:
		manufacturer = Manufacturer.objects.get(name=manufacturer_name)
	except Manufacturer.DoesNotExist:
		manufacturer = Manufacturer(name=manufacturer_name)
		manufacturer.save()
	
	# server type
	try:
		server_type = ServerType.objects.get(name=facts['productname'],
			manufacturer=manufacturer)
	except ServerType.DoesNotExist:
		server_type = ServerType(name=facts['productname'],
			manufacturer=manufacturer)
		server_type.save()

	# architecture
	try:
		os_arch = Architecture.objects.get(name=facts['architecture'])
	except Architecture.DoesNotExist:
		os_arch = Architecture(name=facts['architecture'])
		os_arch.save()

	# operating system
	try:
		operatingsystem = OperatingSystem.objects.get(name=facts['operatingsystem'], version=facts['operatingsystemrelease'], architecture=os_arch)
	except OperatingSystem.DoesNotExist:
		operatingsystem = OperatingSystem(name=facts['operatingsystem'], version=facts['operatingsystemrelease'], architecture=os_arch)
		operatingsystem.save()

	# server
	server = Server()
	server.name = facts['hostname']
	# TODO
	server.memory = facts['memorysize'].split()[0]
	server.serial = facts['serialnumber']
	server.operating_system = operatingsystem
	server.server_type = server_type
	server.save()

	'''
	server type:
		manufacturer -> Dell Inc.
		hardwaremodel -> x86_64
		productname -> PowerEdge R710
	server:
		serialnumber -> 89TSNK1
		operatingsystem -> RedHat
		lsbdistid -> RedHatEnterpriseServer
		operatingsystemrelease -> 5.4
		architecture -> x86_64
		memorysize -> 47.14 GB
	'''

	return HttpResponse('OK')
