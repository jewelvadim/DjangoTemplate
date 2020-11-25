from django.db import models

from ckeditor.fields import RichTextField


class MainConfig(models.Model):
	allow_robots = models.BooleanField(
		verbose_name='Разрешить индексацию?',
		help_text='Если галочка не активна, поисковые роботы не будут индексировать сайт',
		default=False
	)

	# logo
	# address
	# phone
	# social media

	policy = RichTextField(
		verbose_name='Политика конфиденциальности',
		blank=True
	)

	extra_scripts = models.TextField(
		verbose_name='Дополнительные скрипты',
		blank=True
	)

	def __str__(self):
		return 'Основные данные сайта'

	class Meta:
		verbose_name = 'Глобальные настройки'
		verbose_name_plural = 'Глобальные настройки'
