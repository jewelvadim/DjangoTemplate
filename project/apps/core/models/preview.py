from django.db import models
from django.utils.safestring import mark_safe

from apps.core.functions import PathAndRename


class PreviewAbstract(models.Model):
	upload_path = ''

	preview = models.ImageField(
		verbose_name='Превью',
		upload_to=PathAndRename()
	)

	class Meta:
		abstract = True

	def admin_preview(self, width=150, height=150):
		return mark_safe(
			'<img src="{}" style="width: {}px; height: {}px; object-fit: contain;"'.format(
				self.preview.url,
				width,
				height
			)
		)
	admin_preview.short_description = 'Превью'
