from django.views.generic import TemplateView

from apps.main.models import MainConfig


class TextPageAbstractView(TemplateView):
	template_name = 'components/textpage.html'
	page_title = ''
	config = None

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.config = MainConfig.objects.first() or MainConfig.objects.create()

	def get_context_data(self, **kwargs):
		context = super(TextPageAbstractView, self).get_context_data(**kwargs)

		context['breadcrumbs'] = [
			{'title': self.page_title, 'link': ''}
		]
		context['page_content'] = self.get_page_content()

		return context

	def get_page_content(self):
		return self.config
