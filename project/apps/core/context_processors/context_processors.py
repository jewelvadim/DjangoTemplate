from apps.main.models import SeoItem, MainConfig


def context_processors(request):
	try:
		seo_item = SeoItem.objects.get(path=request.path)
	except SeoItem.DoesNotExist:
		seo_item = {}

	config = MainConfig.objects.first() or MainConfig.objects.create()

	return {
		'seo_config': seo_item,
		'config': config
	}
