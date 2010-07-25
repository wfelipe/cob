from django.db import models
"""
configuration items
"""
class ServerType(models.Model):
	name = models.CharField(max_length=255, null=False)
	size = models.IntegerField()

	def __unicode__(self):
		return str(self.name)

class Server(models.Model):
	name = models.CharField(max_length=255, null=False, unique=True)
	memory = models.IntegerField(null=False)
	serial = models.CharField(max_length=255, null=False)
	operating_system = models.ForeignKey('OperatingSystem', null=False)

	server_type = models.ForeignKey('ServerType', null=False)

	def __unicode__(self):
		return str(self.name)

class OperatingSystem(models.Model):
	name = models.CharField(max_length=255, null=False)
	version = models.CharField(max_length=16, null=False)

	class Meta:
		unique_together = [("name", "version")]

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

