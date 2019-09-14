from django.contrib import admin
from .models import Urls

class UrlsAdmin(admin.ModelAdmin):
    list_display = ('fake_url', 'original_url')

admin.site.register(Urls, UrlsAdmin)
