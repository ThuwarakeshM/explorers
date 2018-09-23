from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Adventure, Event, Album
# Create your views here.


def home(request):
    adventures = Adventure.objects.all()[:6]
    return render(request, 'explorers/home.html', {'adventures': adventures})


def about(request):
    return render(request, 'explorers/about.html', {})


def contact(request):
    return render(request, 'explorers/contact.html', {})


def adventures(request):
    advs = Adventure.objects.filter(is_published=True)
    return render(request, 'explorers/adventure_list.html', {'adventures': advs})


def adventure(request, qualifier):
    adv = Adventure.objects.get(page_qualifier=qualifier)
    return render(request, 'explorers/adventure_detail.html', {'adventure': adv})


def events(request):
    evts = Event.objects.filter(is_published=True)
    return render(request, 'explorers/event_list.html', {'events': evts})


def event(request, qualifier):
    evt = Event.objects.get(page_qualifier=qualifier)
    return render(request, 'explorers/event_detail.html', {'event': evt})


def gallery(request):
    albums = Album.objects.filter(is_published=True)
    return render(request, 'explorers/gallery.html', {'albums': albums})


def album(request, qualifier):
    album = Album.objects.get(page_qualifier=qualifier)
    return render(request, 'explorers/album.html', {'album': album})
