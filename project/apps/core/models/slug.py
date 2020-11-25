from django.db import models
from django.urls import reverse


class SlugAbstract(models.Model):
	path_code = 'app:url_pattern_name'

	slug = models.SlugField(
		verbose_name='Адрес в строке браузера',
		max_length=200,
		unique=True,
		db_index=True
	)

	class Meta:
		abstract = True

	def get_absolute_url(self):
		return reverse(self.path_code, args=[self.slug])
