from django.contrib import admin

from apps.main.models import SeoItem, Email


@admin.register(SeoItem)
class SeoItemAdmin(admin.ModelAdmin):
	pass


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
	list_display = ['email', 'is_active']
	list_editable = ['is_active']
