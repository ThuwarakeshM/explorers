from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.ImageSet)
admin.site.register(models.FlatPage)
admin.site.register(models.Adventure)
admin.site.register(models.Event)
admin.site.register(models.Contact)
admin.site.register(models.Album)