from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from settings import DATA_UPLOAD_MAX_MEMORY_SIZE


@deconstructible
class FileSizeValidator:
	def __init__(self, size=None, message=None, code=None):
		self.size = size or DATA_UPLOAD_MAX_MEMORY_SIZE
		if message is not None:
			self.message = message
		else:
			self.message = 'Максимальный размер файла не должен превышать {} MB'.format(self.size / (1024 * 1024))
		if code is not None:
			self.code = code
		else:
			self.code = 'invalid_size'

	def __call__(self, value):
		if value.file.size > self.size:
			raise ValidationError(message=self.message, code=self.code)
