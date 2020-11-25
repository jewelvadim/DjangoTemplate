from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from apps.main.models.managers import ActiveManager
from apps.main.functions import PathAndRename


class OrderAbstract(models.Model):
	order = models.PositiveSmallIntegerField(
		verbose_name='Порядок вывода',
		default=1
	)

	class Meta:
		abstract = True
		ordering = ['order']


class ActiveAbstract(models.Model):
	is_active = models.BooleanField(
		verbose_name='Активный?',
		help_text='Вместо удаления элемента, снимите эту галочку',
		default=True
	)

	objects = models.Manager()
	active_objects = ActiveManager()

	class Meta:
		abstract = True


class SeoAbstract(models.Model):
	seo_title = models.CharField(
		verbose_name='СЕО-заголовок',
		max_length=70,
		blank=True
	)

	seo_description = models.TextField(
		verbose_name='СЕО-описание',
		max_length=140,
		blank=True
	)

	class Meta:
		abstract = True


class TitleAbstract(models.Model):
	title = models.CharField(
		verbose_name='Название',
		max_length=250
	)

	def __str__(self):
		return self.title

	class Meta:
		abstract = True


class CreatedAbstract(models.Model):
	created = models.DateTimeField(
		verbose_name='Дата создания',
		auto_now_add=True
	)

	class Meta:
		abstract = True
		ordering = ['-created']


class SlugAbstract(models.Model):
	path_code = ''

	slug = models.SlugField(
		verbose_name='Адрес в строке браузера',
		max_length=200,
		unique=True
	)

	class Meta:
		abstract = True

	def get_absolute_url(self):
		return reverse(self.path_code, args=[self.slug])


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
