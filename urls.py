from django.urls import path
from . import views

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
]
