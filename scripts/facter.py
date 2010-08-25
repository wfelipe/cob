#!/usr/bin/env python
#
# a script to execute facter and send the data to the cmdb app
#
from subprocess import Popen, PIPE
import httplib, urllib

facterp = Popen("facter", shell=True, stdout=PIPE, stderr=PIPE)
if facterp.wait():
	print "ERROR:", facterp.stderr.readlines()[0]

# strip the --- line
#facterp.stdout.readline()
facts = dict()
#for fact in facterp.stdout:
#	print fact.strip('\n')
#	print fact.split(': ', 1)
facts = dict([ fact.strip('\n').strip().split(' => ', 1) for fact in facterp.stdout ])

#import sys
#sys.exit(0)

conn = httplib.HTTPConnection("localhost:8000")
params = urllib.urlencode(facts)
conn.request("POST", "/cmdb/server/facts/", params)
resp = conn.getresponse()
#print resp.status, resp.reason

print resp.read()
