from django.db import models
import datetime

RR_TYPES = (
	('A', 'Host'),
	('NS', 'Name Server'),
	('CNAME', 'Canonical Name/Alias'),
	('SOA', 'Start of a zone authority'),
	('PTR', 'Name Pointer/Reverse'),
	('MX', 'Mail Exchange'),
	('TXT', 'Text Strings'),
)

class Serial (models.Model):
	domain = models.ForeignKey('Domain', null=False)
	serial = models.IntegerField(null=False)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	class Meta:
		unique_together = (("domain", "serial"),)

class Domain (models.Model):
	name = models.CharField(max_length=255, null=False)
	current_serial = models.ForeignKey(Serial, null=True, related_name='current_serial')
	def __unicode__(self):
		return self.name

class Record (models.Model):
	domain = models.ForeignKey(Domain)
	name = models.CharField(max_length=255, null=True)
	type = models.CharField(max_length=6, choices=RR_TYPES)
	content = models.CharField(max_length=255, null=True)
	ttl = models.IntegerField(default=3600)
	prio = models.IntegerField(default=0)
	since_date = models.DateTimeField(default=datetime.datetime.now)
	out_date = models.DateTimeField(default=datetime.datetime.max)
	def __unicode__(self):
		return self.name
