from cmdb.models import *
from django.contrib import admin

admin.site.register(System)

class OperatingSystemAdmin(admin.ModelAdmin):
	list_display = ['name', 'version']

class InternetAddressAdmin(admin.ModelAdmin):
	list_display = ['address', 'network']

class NetworkInterfaceAdmin(admin.ModelAdmin):
	list_display = ['name', 'macaddress', 'ipaddress', 'server' ]

admin.site.register(Manufacturer)
admin.site.register(Architecture)
admin.site.register(ServerType)
admin.site.register(Server)

admin.site.register(NetworkInterface, NetworkInterfaceAdmin)
admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.register(InternetAddress, InternetAddressAdmin)
