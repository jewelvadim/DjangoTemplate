from django.urls import path

from apps.main.views import IndexTemplateView, PolicyTemplateView


urlpatterns = [
	path('', IndexTemplateView.as_view(), name='index'),
	path('policy/', PolicyTemplateView.as_view(), name='policy')
]
