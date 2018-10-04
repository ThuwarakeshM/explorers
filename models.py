from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField

class PageInfo(models.Model):
    page_title = models.CharField(
        max_length=100, help_text='Limit it to 60-70 characters')
    page_description = models.CharField(
        max_length=200, help_text='Limit it to 160-180 characters')
    page_keywords = models.CharField(
        max_length=100, help_text='Limit it to 10 words')
    page_url = models.CharField(max_length=100)
    page_image = models.CharField(
        max_length=300, help_text='HD image preferable')
    page_qualifier = models.CharField(max_length=25, primary_key=True)

    pub_date = models.DateField(auto_now=True)

    thumbnail = models.CharField(
        max_length=300, help_text='Thumbnail to represent the page', blank=True, null=True)

    def __str__(self):
        return self.page_qualifier

    class Meta:
        abstract = True


class Album(PageInfo):
    internal = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return '/gallary/{}'.format(self.page_qualifier)


class FlatPage(PageInfo):
    def get_absolute_url(self):
        return '/{}'.format(self.page_qualifier)


class ImageSet(models.Model):
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)

    url_desktop = models.CharField(
        max_length=300, help_text='Image to show on desktops')
    url_laptop = models.CharField(
        max_length=300, help_text='Image to show on desktops', blank=True)
    url_tablets = models.CharField(
        max_length=300, help_text='Image to show on desktops', blank=True)
    url_mobile = models.CharField(
        max_length=300, help_text='Image to show on desktops', blank=True)

    image_title = models.CharField(
        max_length=100, help_text='To be displayed on top of the image')
    image_alt = models.CharField(
        max_length=100, help_text='To be displayed if image not found and for SEO purposes')

    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.image_title

    def save(self, *args, **kwargs):
        if not self.url_laptop:
            self.url_laptop = self.url_desktop
        if not self.url_tablets:
            self.url_tablets = self.url_laptop
        if not self.url_mobile:
            self.url_mobile = self.url_tablets

        # Call the real save() method
        super().save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('email', 'phone',)


class Activity(PageInfo):
    image = models.ForeignKey(ImageSet, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    description = models.TextField()
    eligibility = models.TextField()
    preparation = models.TextField()
    cost = models.IntegerField()

    instructor = models.ForeignKey(Contact, on_delete=models.PROTECT)

    is_published = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Adventure(Activity):

    def get_absolute_url(self):
        return '/adventures/{}'.format(self.page_qualifier)


class Event(Activity):
    event_start_date = models.DateTimeField(default= timezone.now)
    event_end_date = models.DateField(default= timezone.now)
    event_start_time = models.TimeField(default= timezone.now)
    event_start_place = models.CharField(max_length=100, default= "Fort Railway Station")
    event_destination = models.CharField(max_length=100, default = "Adventure Explorers, Kitulgala")

    def get_absolute_url(self):
        return '/events/{}'.format(self.page_qualifier)

class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()


class Article(PageInfo):
    content = MarkdownxField()
    created = models.DateField(auto_now_add=True)
    published = models.BooleanField()