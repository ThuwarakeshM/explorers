from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Adventure, Event, Album, FlatPage, ImageSet
# Create your views here.


def home(request):
    page = FlatPage.objects.get(page_qualifier='home')
    adventures = Adventure.objects.all()[:6]
    album = Album.objects.get(page_qualifier='carousel')
    carousel = ImageSet.objects.filter(album = album)
    return render(request, 'explorers/home.html', {
        'adventures': adventures,
        'page': page,
        'carousel': carousel
    })


def about(request):
    page = FlatPage.objects.get(page_qualifier='about')
    return render(request, 'explorers/about.html', {'page': page})


def contact(request):
    page = FlatPage.objects.get(page_qualifier='contact')
    return render(request, 'explorers/contact.html', {'page': page})


def adventures(request):
    advs = Adventure.objects.filter(is_published=True)
    return render(request, 'explorers/adventure_list.html', {'adventures': advs})


def adventure(request, qualifier):
    adv = Adventure.objects.get(page_qualifier=qualifier)
    adv.description = adv.description.split('|')
    adv.eligibility = adv.eligibility.split('|')
    adv.preparation = adv.preparation.split('|')
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
