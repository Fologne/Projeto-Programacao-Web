from django.contrib import admin
from banner.models import Banner

# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug': ('titulo',)
    }
    list_display = ('titulo',)
admin.site.register(Banner, BannerAdmin)