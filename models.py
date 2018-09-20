from django.db import models

# Create your models here.


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

    def __str__(self):
        return self.page_qualifier

    class Meta:
        abstract=True

class MainPage(PageInfo):
    def get_absolute_url(self):
        return '/{}'.format(self    .page_qualifier)


class ImageSet(models.Model):
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
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    staff = models.BooleanField()

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

    class Meta:
        abstract=True

class Adventure(Activity):

    def get_absolute_url(self):
        return '/adventures/{}'.format(self.page_qualifier)
    

class Event(Activity):

    def get_absolute_url(self):
        return '/events/{}'.format(self.page_qualifier)
