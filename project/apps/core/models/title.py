from django.db import models


class TitleAbstract(models.Model):
	title = models.CharField(
		verbose_name='Название',
		max_length=250
	)

	def __str__(self):
		return self.title

	class Meta:
		abstract = True
