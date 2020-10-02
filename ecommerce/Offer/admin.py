from django.contrib import admin
from . import models
from django.conf import settings

admin.site.register(models.OfferCategory)

class OfferAdmin(admin.ModelAdmin):
    if settings.MULTI_VENDOR:
        list_display = ['title', 'total_vendors', 'starting_from']
        list_filter = ('vendor',)
    else:
        list_display = ['title', 'create_at', 'starting_from']

    list_per_page = 25
    search_fields = ['title', 'description']
    readonly_fields = ['big_banner_tag', 'small_banner_tag']
    # autocomplete_fields = ['category']

admin.site.register(models.Offer, OfferAdmin)