"""abccar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from core.views import listagem_clientes, Registrar, tabela, \
listagem_veiculos, cadastro_veiculo, cadastro_cliente, home, atualiza_cliente, exclui_cliente, atualiza_veiculo, \
exclui_veiculo, listagem_rotativos, cadastro_rotativo, atualiza_rotativo, cadastro_mensalista, listagem_mensalistas, \
exclui_mensalista, atualiza_mensalista, exclui_rotativo, cadastro_parametro, listagem_parametros, \
exclui_parametro, atualiza_parametro

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('', home, name='url_principal'),
    path('cadastro_cliente/', cadastro_cliente, name='url_cadastro_cliente'),
    path('listagem_clientes/', listagem_clientes, name='url_listagem_clientes'),
    path('cadastro_veiculo/', cadastro_veiculo, name='url_cadastro_veiculo'),
    path('listagem_veiculos/', listagem_veiculos, name='url_listagem_veiculos'),
    path('atualiza_cliente/<int:id>/', atualiza_cliente, name='url_atualiza_cliente'),
    path('exclui_cliente/<int:id>', exclui_cliente, name='url_exclui_cliente'),
    path('atualiza_veiculo/<int:id>/', atualiza_veiculo, name='url_atualiza_veiculo'),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name='url_exclui_veiculo'),
    path('listagem_rotativos/', listagem_rotativos, name='url_listagem_rotativos'),
    path('cadastro_rotativo/', cadastro_rotativo, name='url_cadastro_rotativo'),
    path('atualiza_rotativo/<int:id>/', atualiza_rotativo, name='url_atualiza_rotativo'),
    path('cadastro_mensalista/', cadastro_mensalista, name='url_cadastro_mensalista'),
    path('listagem_mensalistas/', listagem_mensalistas, name='url_listagem_mensalistas'),
    path('exclui_mensalista/<int:id>/', exclui_mensalista, name='url_exclui_mensalista'),
    path('atualiza_mensalista/<int:id>/', atualiza_mensalista, name='url_atualiza_mensalista'),
    path('exclui_rotativo/<int:id>/', exclui_rotativo, name='url_exclui_rotativo'),
    path('cadastro_parametro/', cadastro_parametro, name='url_cadastro_parametro'),
    path('listagem_parametros/', listagem_parametros, name='url_listagem_parametros'),
    path('exclui_parametros/<int:id>/', exclui_parametro, name='url_exclui_parametro'),
    path('atualiza_parametro/<int:id>/', atualiza_parametro, name='url_atualiza_parametro'),
    path('tabela/', tabela, name='url_tabela')
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
