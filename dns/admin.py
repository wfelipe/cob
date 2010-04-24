from cob.dns.models import *
from django.contrib import admin

class DomainAdmin(admin.ModelAdmin):
	list_display = ['name']

class RecordAdmin(admin.ModelAdmin):
	list_display = ['name', 'type', 'domain', 'content']

class SerialAdmin(admin.ModelAdmin):
	list_display = ['serial', 'domain']

class DomainSerialAdmin(admin.ModelAdmin):
	list_display = ['domain', 'serial']

admin.site.register(Domain, DomainAdmin)
admin.site.register(Serial, SerialAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(DomainSerial, DomainSerialAdmin)
