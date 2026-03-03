from django.contrib import admin
from produto.models import Produto

# Register your models here.
class ProdutoAdmin (admin.ModelAdmin):
    prepopulated_fields ={
        'slug': ('nome',)
    }
admin.site.register(Produto, ProdutoAdmin)