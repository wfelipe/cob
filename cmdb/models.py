from django.db import models
"""
configuration items
"""
class Manufacturer(models.Model):
	name = models.CharField(max_length=255, null=False)

	def __unicode__(self):
		return str(self.name)

class Architecture(models.Model):
	name = models.CharField(max_length=255, null=False)

	def __unicode__(self):
		return str(self.name)

class ServerType(models.Model):
	name = models.CharField(max_length=255, null=False)
	manufacturer = models.ForeignKey('Manufacturer', null=True)

	def __unicode__(self):
		return str(self.name)

class Server(models.Model):
	name = models.CharField(max_length=255, null=False, unique=True)
	memory = models.FloatField(null=False)
	serial = models.CharField(max_length=255, null=True, default=None)
	virtual = models.BooleanField(null=False)

	operating_system = models.ForeignKey('OperatingSystem', null=False)
	server_type = models.ForeignKey('ServerType', null=False)
	system = models.ForeignKey('System', null=True)

	def __unicode__(self):
		return str(self.name)

class OperatingSystem(models.Model):
	name = models.CharField(max_length=255, null=False)
	version = models.CharField(max_length=16, null=False)
	architecture = models.ForeignKey('Architecture', null=False)

	class Meta:
		unique_together = [("name", "version", "architecture")]

	def __unicode__(self):
		return str(self.name)

class NetworkInterface(models.Model):
	name = models.CharField(max_length=8, null=False)
	macaddress = models.CharField(max_length=18)

	ipaddress = models.ForeignKey('InternetAddress', unique=True)
	server = models.ForeignKey('Server', null=False)

	def __unicode__(self):
		return str(self.name)

class InternetAddress(models.Model):
	address = models.CharField(max_length=255, null=False, unique=True)

	network = models.ForeignKey('Network', null=False)

	def __unicode__(self):
		return str(self.address)

class Network(models.Model):
	name = models.CharField(max_length=255, null=False)
	netmask = models.CharField(max_length=255, null=False)
	network = models.CharField(max_length=255, null=False)

	def __unicode__(self):
		return str(self.name)

"""
Puppet Class, automation
"""
class PuppetClass(models.Model):
	name = models.CharField(max_length=255, null=False, unique=True)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return str(self.name)

"""
System
"""
class System(models.Model):
	name = models.CharField(max_length=255, null=False, unique=True)
	description = models.CharField(max_length=255, null=True)

	puppetclass = models.ManyToManyField(PuppetClass, through='SystemPuppetClass')

	def __unicode__(self):
		return str(self.name)

class SystemPuppetClass(models.Model):
	system = models.ForeignKey(System, null=False)
	puppetclass = models.ForeignKey(PuppetClass, null=False)

	def __unicode__(self):
		return(self.system.name)
