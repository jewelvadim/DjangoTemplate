import os
import time

from django import template

from sorl.thumbnail import get_thumbnail

from settings import STATIC_URL, STATIC_ROOT


register = template.Library()


@register.filter()
def make_thumb(value, size):
	if value:
		return get_thumbnail(value, size).url
	return False


@register.simple_tag
def sstatic(path):
	full_path = os.path.join(STATIC_ROOT, path)
	try:
		mtime = time.strftime("%d.%m.%Y-%H.%M", time.gmtime(os.path.getmtime(full_path)))
		return '{}{}?{}'.format(STATIC_URL, path, mtime)
	except OSError:
		return '{}{}'.format(STATIC_URL, path)


@register.filter()
def prettify_phone(value):
	return '{} ({}) {}-{}-{}'.format(
		value[:2],
		value[2:5],
		value[5:8],
		value[8:10],
		value[10:12]
	)


@register.simple_tag(takes_context=True)
def update_url(context, **kwargs):
	query = context['request'].GET.dict()
	query.update(kwargs)
	return urlencode(query)
