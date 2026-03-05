from django.contrib import admin
from tipo.models import Tipo

# Register your models here.
class TipoAdmin (admin.ModelAdmin):
    prepopulated_fields ={
        'slug': ('nome',)
    }
admin.site.register(Tipo, TipoAdmin)