from django.db import models

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
	serial = models.IntegerField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

class Domain (models.Model):
	name = models.CharField(max_length=255, null=False)
	current_serial = models.ForeignKey(Serial, null=True, related_name='current_serial')

class Record (models.Model):
	domain = models.ForeignKey(Domain)
	name = models.CharField(max_length=255, null=True)
	type = models.CharField(max_length=6, choices=RR_TYPES)
	content = models.CharField(max_length=255, null=True)
	ttl = models.IntegerField()
	prio = models.IntegerField()
	since_date = models.DateTimeField()
	out_date = models.DateTimeField()

#class SuperMaster (models.Model):
#	nameserver
#	account
