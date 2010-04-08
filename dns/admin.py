from cob.dns.models import *
from django.contrib import admin

class DomainAdmin(admin.ModelAdmin):
	list_display = ['name']

class RecordAdmin(admin.ModelAdmin):
	list_display = ['name', 'domain']

class SerialAdmin(admin.ModelAdmin):
	list_display = ['serial', 'domain']

admin.site.register(Domain, DomainAdmin)
admin.site.register(Serial, SerialAdmin)
admin.site.register(Record, RecordAdmin)
