"""
URL configuration for rhapsody project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from rhapsody import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.visualizarHome, name='visualizarHome'),
    path('cadastro-produto', views.cadastroProdutos, name='cadastroProdutos'),
    path('produto/<slug:slug>/', views.visualizarProduto, name='produto'),
    path('categoria/<slug:slug>/', views.produtosPorCategoria, name='categoria'),
    path('tipo/<slug:slug>/', views.produtosPorTipo, name='tipo'),
    path('lista-produtos/', views.listaProduto, name='listaProduto'),
    path('alteraProduto/<slug:slug>/', views.alteraProduto, name='alteraProduto'),
    path('cadastro-banner/', views.cadastroBanner, name='cadastroBanner'),
    path('lista-banners/', views.listaBanner, name='listaBanner'),
    path('alteraBanner/<slug:slug>/', views.alteraBanner, name='alteraBanner'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#esse static é para que o django consiga achar as imagens relacionadas
