from cmdb.models import *
from django.contrib import admin

"""
System <-> PuppetClass
"""
class SystemPuppetClassInline(admin.TabularInline):
	model = SystemPuppetClass
	extra = 1

"""
basic admin classes
"""
class OperatingSystemAdmin(admin.ModelAdmin):
	list_display = ['name', 'version']

class InternetAddressAdmin(admin.ModelAdmin):
	list_display = ['address', 'network']

class NetworkInterfaceAdmin(admin.ModelAdmin):
	list_display = ['name', 'macaddress', 'ipaddress', 'server' ]

class SystemAdmin(admin.ModelAdmin):
	inlines = (SystemPuppetClassInline, )

class PuppetClassAdmin(admin.ModelAdmin):
	inlines = (SystemPuppetClassInline, )

admin.site.register(Manufacturer)
admin.site.register(Architecture)
admin.site.register(ServerType)
admin.site.register(Server)
admin.site.register(SystemPuppetClass)

admin.site.register(System, SystemAdmin)
admin.site.register(PuppetClass, PuppetClassAdmin)
admin.site.register(NetworkInterface, NetworkInterfaceAdmin)
admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.register(InternetAddress, InternetAddressAdmin)
