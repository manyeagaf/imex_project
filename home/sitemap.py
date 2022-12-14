from django.contrib.sitemaps import Sitemap
from .models import Blog

class BlogSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5
    def items(self):
        return Blog.objects.all()
    def lastmod(self, obj):
        return obj.created_on

    def location(self, obj):
        return obj.get_absolute_url()
