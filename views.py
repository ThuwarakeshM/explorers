from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Adventure, Event, Album, FlatPage, ImageSet, Query, Article, Packages
from .forms import ContactForm
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.shortcuts import get_object_or_404, get_list_or_404


def policies(request):
    page = get_object_or_404(FlatPage, page_qualifier='policies')
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
    page = get_object_or_404(FlatPage, page_qualifier='home')
    adventures = get_list_or_404(Adventure, is_published=True)[:6]
    # adventures = Adventure.objects.filter(is_published=True)[:6]
    album = get_object_or_404(Album, page_qualifier='carousel')
    # album = Album.objects.get(page_qualifier='carousel')
    carousel = get_list_or_404(ImageSet,  album=album)
    # carousel = ImageSet.objects.filter(album=album)
    return render(request, 'explorers/home.html', {
        'adventures': adventures,
        'page': page,
        'carousel': carousel
    })


def about(request):
    # page = FlatPage.objects.get(page_qualifier='about')
    page = get_object_or_404(FlatPage, page_qualifier='about')

    return render(request, 'explorers/about.html', {'page': page})


def contact(request):
    form = ContactForm()
    # page = FlatPage.objects.get(page_qualifier='contact')
    page = get_object_or_404(FlatPage, page_qualifier='contact')

    return render(request, 'explorers/contact.html', {'page': page, 'form': form})


def adventures(request):
    # advs = Adventure.objects.filter(is_published=True)
    advs = get_list_or_404(Adventure, is_published=True)
    # page = FlatPage.objects.get(page_qualifier='adventures')
    page = get_object_or_404(FlatPage, page_qualifier='adventure')

    return render(request, 'explorers/adventure_list.html', {'adventures': advs, 'page': page})


def adventure(request, qualifier):
    adv = get_object_or_404(Adventure, page_qualifier=qualifier)
    # adv = Adventure.objects.get(page_qualifier=qualifier)
    adv.description = adv.description.split('|')
    adv.eligibility = adv.eligibility.split('|')
    adv.preparation = adv.preparation.split('|')
    return render(request, 'explorers/adventure_detail.html', {'adventure': adv, 'page': adv})


def events(request):
    # evts = Event.objects.filter(is_published=True)
    # page = FlatPage.objects.get(page_qualifier='events')

    evts = get_list_or_404(Event, is_published=True)
    page = get_object_or_404(FlatPage, page_qualifier='events')
    return render(request, 'explorers/event_list.html', {'events': evts, 'page': page})


def event(request, qualifier):
    evt = get_object_or_404(Event, page_qualifier=qualifier)
    # evt = Event.objects.get(page_qualifier=qualifier)
    evt.description = evt.description.split('|')
    evt.eligibility = evt.eligibility.split('|')
    evt.preparation = evt.preparation.split('|')
    finished = ((evt.event_end_date - timezone.now().date()).days < 0)
    return render(request, 'explorers/event_detail.html', {'event': evt, 'page': evt, 'status': finished})


def gallery(request):
    # albums = Album.objects.filter(is_published=True)
    albums = get_list_or_404(Album, is_published=True)
    return render(request, 'explorers/gallery.html', {'albums': albums})


def album(request, qualifier):
    # album = Album.objects.get(page_qualifier=qualifier)
    album = get_object_or_404(Album, page_qualifier=qualifier)
    # images = ImageSet.objects.filter(album=album)
    images = get_list_or_404(ImageSet, album=album)
    return render(request, 'explorers/album.html', {'images': images})


def article(request, qualifier):
    # article = Article.objects.get(page_qualifier=qualifier)
    article = get_object_or_404(Article, page_qualifier=qualifier)
    return render(request, 'explorers/article.html', {'page': article})


def articles(request):
    # page = FlatPage.objects.get(page_qualifier='articles')
    page = get_object_or_404(FlatPage, page_qualifier='articles')
    # arts = Article.objects.filter(is_published=True)
    arts = get_list_or_404(Article, is_published=True)
    return render(request, 'explorers/articles.html', {'page': page, 'articles': arts})

def packages(request):
    # page = FlatPage.objects.get(page_qualifier='packages')
    page = get_object_or_404(FlatPage, page_qualifier='packages')
    # pkgs = Packages.objects.filter(is_published=True)
    pkgs = get_list_or_404(Packages, is_published=True)
    return render(request, 'explorers/packages.html', {'packages': pkgs, 'page': page})

def package(request, qualifier):
    # pkg = Packages.objects.get(page_qualifier=qualifier)
    pkg = get_object_or_404(page_qualifier=qualifier)
    return render(request, 'explorers/package.html', {'page': pkg})