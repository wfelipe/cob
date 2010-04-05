from cob.dns.models import *
from django.contrib import admin

admin.site.register(Domain)
admin.site.register(Serial)
class RecordAdmin(admin.ModelAdmin):
	list_display = ['name', 'domain']
admin.site.register(Record, RecordAdmin)
