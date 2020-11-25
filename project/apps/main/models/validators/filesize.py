from django.core.exceptions import ValidationError

from settings import DATA_UPLOAD_MAX_MEMORY_SIZE


def filesize_validator(file):
	if file.file.size > DATA_UPLOAD_MAX_MEMORY_SIZE:
		raise ValidationError(
			'Максимальный размер файла не должен превышать {} MB'.format(DATA_UPLOAD_MAX_MEMORY_SIZE / (1024 * 1024))
		)
