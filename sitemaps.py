from django.contrib.sitemaps import Sitemap
from .models import FlatPage, Adventure, Event

class PageSiteMap(Sitemap):
    changeferq="weekly"
    priority=0.5
    protocol="https"

    def items(self):
        return FlatPage.objects.all()

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