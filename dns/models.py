from django.db import models
import datetime

RR_TYPES = (
	('A', 'A'),		# Host
	('NS', 'NS'),		# Name Server
	('CNAME', 'CNAME'),	# Canonical Name/Alias
	('SOA', 'SOA'),		# Start of a zone authority
	('PTR', 'PTR'),		# Name Pointer/Reverse
	('MX', 'MX'),		# Mail Exchange
	('TXT', 'TXT'),		# Text Strings
)

class Serial (models.Model):
	domain = models.ForeignKey('Domain', null=False)
	serial = models.IntegerField(null=False)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField(default=datetime.datetime.now)

	class Meta:
		unique_together = [("domain", "serial")]

	def __unicode__(self):
		return str(self.serial)

class Domain (models.Model):
	name = models.CharField(max_length=100, null=False, unique=True, blank=False)
	# pattern to create serials
	# the goal is to be YYYYMMDDxx (where xx is incremental)
	serial_pattern = models.CharField(max_length=100)
	# SOA definitions
	source = models.CharField(max_length=100, null=False)
	contact = models.CharField(max_length=100, null=False)
	refresh = models.IntegerField(null=False, default=3600)
	retry = models.IntegerField(null=False, default=600)
	expire = models.IntegerField(null=False, default=84600)
	ttl = models.IntegerField(null=False, default=3600)

	def __unicode__(self):
		return self.name

class Record (models.Model):
	domain = models.ForeignKey(Domain)
	name = models.CharField(max_length=255, null=True)
	# fullname = name.domain
	fullname = models.CharField(max_length=255, null=True)
	type = models.CharField(max_length=6, choices=RR_TYPES)
	content = models.CharField(max_length=255, null=True)
	ttl = models.IntegerField(default=3600)
	prio = models.IntegerField(default=0)
	since_date = models.DateTimeField(default=datetime.datetime.now)
	out_date = models.DateTimeField(default=datetime.datetime.max)

	def __unicode__(self):
		return self.name

#
# current serial
#
class DomainSerial (models.Model):
	domain = models.ForeignKey(Domain, null=False, unique=True)
	serial = models.ForeignKey(Serial, null=False, unique=True)
