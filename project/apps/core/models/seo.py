from django.db import models


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
