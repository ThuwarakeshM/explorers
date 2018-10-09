from django.contrib import admin
from . import models
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
admin.site.register(models.ImageSet)
admin.site.register(models.FlatPage)
admin.site.register(models.Adventure)
admin.site.register(models.Event)
admin.site.register(models.Contact)
admin.site.register(models.Album)
admin.site.register(models.Query)
admin.site.register(models.Article, MarkdownxModelAdmin)
admin.site.register(models.Packages, MarkdownxModelAdmin)