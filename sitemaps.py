from django.contrib.sitemaps import Sitemap
from .models import FlatPage, Adventure, Event, Article

class PageSiteMap(Sitemap):
    changeferq="weekly"
    priority=0.5
    protocol="https"

    def items(self):
        return FlatPage.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.pub_date

class AdventureSiteMap(Sitemap):
    changeferq="weekly"
    priority=0.8
    protocol="https"

    def items(self):
        return Adventure.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

class EventSiteMap(Sitemap):
    changeferq="weekly"
    priority=0.6
    protocol="https"

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

class ArticleSiteMap(Sitemap):
    changefreq="never"
    priority=0.6
    protocol='https'

    def items(self):
        return Article.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.pub_date