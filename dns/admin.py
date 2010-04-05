from cob.dns.models import *
from django.contrib import admin

class DomainAdmin(admin.ModelAdmin):
	list_display = ['name', 'current_serial']
class RecordAdmin(admin.ModelAdmin):
	list_display = ['name', 'domain']
admin.site.register(Domain, DomainAdmin)
admin.site.register(Serial)
admin.site.register(Record, RecordAdmin)
