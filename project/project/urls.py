from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from settings import MEDIA_URL, MEDIA_ROOT

from project.sitemaps import sitemaps


urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('apps.main.urls')),
	path('ckeditor/', include('ckeditor_uploader.urls')),
	path('robots.txt', include('robots.urls')),
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
