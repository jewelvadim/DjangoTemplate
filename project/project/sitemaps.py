from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class SitemapMixin(Sitemap):
    priority = 0.9
    changefreq = 'weekly'
    model_class = None
    protocol = 'https'

    def items(self):
        return self.model_class.active_objects.all()

    def location(self, obj):
        return obj.get_absolute_url()


class StaticViewSitemap(SitemapMixin):
    def items(self):
        return ['index', 'policy']

    def location(self, item):
        return reverse(item)


sitemaps = {
    'static': StaticViewSitemap
}
