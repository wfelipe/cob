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

def generate_soa(domainserial):
	return "%s. %s. %d %d %d %d %d" % (
		domainserial.domain.source,
		domainserial.domain.contact,
		domainserial.serial.serial,
		domainserial.domain.refresh,
		domainserial.domain.retry,
		domainserial.domain.expire,
		domainserial.domain.ttl,
	)
