from django.db import models


class OrderAbstract(models.Model):
	order = models.PositiveSmallIntegerField(
		verbose_name='Порядок вывода',
		default=1
	)

	class Meta:
		abstract = True
		ordering = ['order']
