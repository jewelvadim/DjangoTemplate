import os

from uuid import uuid4

from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename(object):
	def __init__(self, sub_path=None):
		self.path = sub_path

	def __call__(self, instance, filename):
		ext = filename.split('.')[-1]
		if instance.pk:
			filename = '{}.{}'.format(instance.pk, ext)
		else:
			filename = '{}.{}'.format(uuid4().hex, ext)

		upload_path = self.path or instance.upload_path

		return os.path.join(upload_path, filename)
