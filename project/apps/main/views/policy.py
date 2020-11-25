from django.views.generic import TemplateView


class PolicyTemplateView(TemplateView):
	template_name = 'pages/policy/index.html'
