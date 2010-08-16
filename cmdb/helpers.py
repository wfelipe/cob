from django.shortcuts import _get_queryset

def normalize_memory(memory):
	"""
	receives the string 'X.XX GB', converts to MB, and return a float
	"""
	memory, size = memory.split()
	memory = float(memory)
	if size == 'GB':
		return memory * 1024
	elif size == 'MB':
		return memory

	return memory

def get_object_or_none(klass, *args, **kwargs):
	"""
	get an object or return a new object
	"""
	queryset = _get_queryset(klass)
	try:
		return queryset.get(*args, **kwargs)
	except queryset.model.DoesNotExist:
		return None

def get_object_or_new(klass, *args, **kwargs):
	"""
	get an object or return a new object
	"""
	obj = get_object_or_none(klass, *args, **kwargs)
	if obj:
		return obj
	else:
	 	return klass()

def get_object_or_create(klass, *args, **kwargs):
	"""
	get an object or return a new object
	"""
	obj = get_object_or_none(klass, *args, **kwargs)
	if obj:
		return obj
	else:
	 	obj = klass()
		for attr in kwargs:
			setattr(obj, attr, kwargs[attr])
		obj.save()
		return obj

def create_network(network, netmask, name=None):
	from cmdb.models import Network
#	import socket, struct
	"""
	creates a new network, and the ip addresses that are inside the network
	"""

	if not name: name = network

	network = Network(name=name, network=network,
		netmask=netmask)
	network.save()

	# TODO - create the ip addresses
	return network
