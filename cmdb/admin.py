from cmdb.models import *
from django.contrib import admin

admin.site.register(System)
admin.site.register(Component)

class OperatingSystemAdmin(admin.ModelAdmin):
	list_display = ['name', 'version']

class InternetAddressAdmin(admin.ModelAdmin):
	list_display = ['address', 'network']

admin.site.register(Manufacturer)
admin.site.register(Architecture)
admin.site.register(ServerType)
admin.site.register(Server)

admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.register(InternetAddress, InternetAddressAdmin)
