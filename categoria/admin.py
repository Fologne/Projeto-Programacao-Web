from django.contrib import admin
from categoria.models import Categoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug': ('nome',)
    }
    list_display = ('nome', 'descricao')
admin.site.register(Categoria, CategoriaAdmin)