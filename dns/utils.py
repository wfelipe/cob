from cob.dns.models import *
import datetime

def generate_serial(last, pattern=''):
	return last + 1

def create_record(domain, name, type, content, ttl=3600, prio=0):
	record = Record(domain=domain)

	record.name = name
	record.fullname = "%s.%s" % (name, domain)
	record.type = type
	record.content = content
	record.ttl = ttl
	record.prio = prio

	return record
