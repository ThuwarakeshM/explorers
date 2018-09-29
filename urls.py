from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PageSiteMap, AdventureSiteMap, EventSiteMap


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('adventures', views.adventures, name='adventures'),
    path('adventures/<str:qualifier>/',
         views.adventure, name='adventure'),
    path('events', views.events, name='events'),
    path('events/<str:qualifier>/',
         views.event, name='event'),
    path('gallery', views.gallery, name='gallery'),
    path('album/<str:qualifier>/', views.album, name='album'),
    path('contact_form', views.contact_form, name='contact_form'),
    path('thanks', views.thanks, name='thanks'),
    path('policies', views.policies, name='policies'),
    path('sitemap.xml', sitemap, {'sitemaps': {
        'pages': PageSiteMap,
        'activities': AdventureSiteMap,
        'events': EventSiteMap,
    }},
     name='django.contrib.sitemaps.views.sitemap')
]
