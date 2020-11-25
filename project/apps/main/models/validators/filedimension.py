from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.core.files.images import get_image_dimensions


@deconstructible
class FileDimensionValidator:
	def __init__(self, width=None, height=None, message=None, code=None):
		if width is not None:
			self.width = width
		if height is not None:
			self.height = height
		if message is not None:
			self.message = message
		else:
			self.message = 'Размеры изображения должны быть не менее {}x{}'.format(self.width, self.height)
		if code is not None:
			self.code = code
		else:
			self.code = 'invalid_dimension'

	def __call__(self, value):
		width, height = get_image_dimensions(value.file)
		if width < self.width or height < self.height:
			raise ValidationError(message=self.message, code=self.code)
