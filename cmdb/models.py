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
	serial = models.CharField(max_length=255, null=False)
	operating_system = models.ForeignKey('OperatingSystem', null=False)

	server_type = models.ForeignKey('ServerType', null=False)

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

"""
System
"""
class System(models.Model):
	name = models.CharField(max_length=255, null=False, unique=True)
	description = models.CharField(max_length=255, null=True)

	def __unicode__(self):
		return str(self.name)

class Component(models.Model):
	name = models.CharField(max_length=255, null=False)
	description = models.CharField(max_length=255, null=True)

	system = models.ForeignKey('System', null=False)
	servers = models.ManyToManyField(Server)

	class Meta:
		unique_together = [("name", "system")]

	def __unicode__(self):
		return str(self.name)

