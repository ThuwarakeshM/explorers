from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Adventure, Event, Album, FlatPage, ImageSet, Query, Article
from .forms import ContactForm
from django.views.decorators.http import require_POST
from django.utils import timezone


def policies(request):
    page = FlatPage.objects.get(page_qualifier='policies')
    return render(request, 'explorers/policies.html', {'page': page})


def thanks(request):
    return render(request, 'explorers/thanks.html', {})


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            q = Query(
                name=data['name'],
                phone=data['phone'],
                message=data['message'],
                email=data['email']
            )

            q.save()
            return HttpResponseRedirect('/thanks')
    return HttpResponseRedirect('/contact/?invalid=1')


def home(request):
    page = FlatPage.objects.get(page_qualifier='home')
    adventures = Adventure.objects.all()[:6]
    album = Album.objects.get(page_qualifier='carousel')
    carousel = ImageSet.objects.filter(album=album)
    return render(request, 'explorers/home.html', {
        'adventures': adventures,
        'page': page,
        'carousel': carousel
    })


def about(request):
    page = FlatPage.objects.get(page_qualifier='about')
    return render(request, 'explorers/about.html', {'page': page})


def contact(request):
    form = ContactForm()
    page = FlatPage.objects.get(page_qualifier='contact')
    return render(request, 'explorers/contact.html', {'page': page, 'form': form})


def adventures(request):
    advs = Adventure.objects.filter(is_published=True)
    page = FlatPage.objects.get(page_qualifier='adventures')
    return render(request, 'explorers/adventure_list.html', {'adventures': advs, 'page': page})


def adventure(request, qualifier):
    adv = Adventure.objects.get(page_qualifier=qualifier)
    adv.description = adv.description.split('|')
    adv.eligibility = adv.eligibility.split('|')
    adv.preparation = adv.preparation.split('|')
    return render(request, 'explorers/adventure_detail.html', {'adventure': adv, 'page': adv})


def events(request):
    evts = Event.objects.filter(is_published=True)
    page = FlatPage.objects.get(page_qualifier='events')
    return render(request, 'explorers/event_list.html', {'events': evts, 'page': page})


def event(request, qualifier):
    evt = Event.objects.get(page_qualifier=qualifier)
    evt.description = evt.description.split('|')
    evt.eligibility = evt.eligibility.split('|')
    evt.preparation = evt.preparation.split('|')
    finished = ((evt.event_end_date - timezone.now().date()).days < 0)
    return render(request, 'explorers/event_detail.html', {'event': evt, 'page': evt, 'status': finished})


def gallery(request):
    albums = Album.objects.filter(is_published=True)
    return render(request, 'explorers/gallery.html', {'albums': albums})


def album(request, qualifier):
    album = Album.objects.get(page_qualifier=qualifier)
    images = ImageSet.objects.filter(album=album)
    return render(request, 'explorers/album.html', {'images': images})


def article(request, qualifier):
    article = Article.objects.get(page_qualifier=qualifier)
    return render(request, 'explorers/article.html', {'page': article})


def articles(request):
    page = FlatPage.objects.get(page_qualifier='articles')
    arts = Article.objects.filter(is_published=True)
    return render(request, 'explorers/articles.html', {'page': page, 'articles': arts})