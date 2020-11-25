from django.db import models

from apps.main.models import SeoAbstract, ActiveAbstract


class SeoItem(SeoAbstract):
	path = models.CharField(
		verbose_name='Путь',
		max_length=150,
		unique=True,
		help_text='/section/item/'
	)

	def __str__(self):
		return self.path

	class Meta:
		verbose_name = 'Элемент сео'
		verbose_name_plural = 'Элементы сео'


class Email(ActiveAbstract):
	email = models.EmailField(
		verbose_name='Почтовый адрес',
		max_length=100
	)

	def __str__(self):
		return self.email

	class Meta:
		verbose_name = 'Почтовый адрес'
		verbose_name_plural = 'Почтовые адреса'
