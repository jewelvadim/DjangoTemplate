from apps.core.views import TextPageAbstractView


class PolicyTemplateView(TextPageAbstractView):
	page_title = 'Политика конфиденциальности'

	def get_page_content(self):
		page_content = super().get_page_content()

		return page_content.policy
