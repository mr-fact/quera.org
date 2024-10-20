from django.contrib import admin

from .models import BlockedIp, SecurityConfig, ViewDetail


# Register your models here.

@admin.register(BlockedIp)
class BlockedIpAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'rps', 'view', 'ban_time', 'created_at')

    search_fields = ('ip', 'view__name', 'view__path')
    list_filter = ('view', )

    list_display_links = ('id', 'ip')


@admin.register(SecurityConfig)
class SecurityConfigAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False



@admin.register(ViewDetail)
class ViewDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'path')

    search_fields = ('name', 'path')

    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False
