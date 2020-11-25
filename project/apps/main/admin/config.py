from django.contrib import admin

from apps.main.models import MainConfig


@admin.register(MainConfig)
class MainConfigAdmin(admin.ModelAdmin):
	def has_delete_permission(self, request, obj=None):
		return False

	def has_add_permission(self, request):
		return False
