from django.db import models

from apps.core.models.managers import ActiveManager


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
