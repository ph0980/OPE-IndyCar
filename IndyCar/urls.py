"""IndyCar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path,path
from funilaria.views import *
from funilaria import views as funilaria_views
from usuario import views as usuario_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [

    path('paginainicial/', funilaria_views.pagina_inicial),
    url(r'status/busca/',status_ordem,name='status_ordem'),
    path('quemsomos/', funilaria_views.quemsomos),
    path('index/', funilaria_views.index),
    path('admin/', admin.site.urls),
    path('clientes/',cliente,name='cliente'),
    url(r'clientes/busca/',cliente,name='busca_cliente'),
   
    path('',funilaria_views.pagina_inicial),
    re_path(r'cliente/(?P<id>\d+)/$',funilaria_views.editar_cliente, name='editar_cliente'),
    re_path(r'cliente/deletar/(?P<id>\d+)/$',funilaria_views.deletar_cliente, name='deletar_cliente'),
    path('cliente/', funilaria_views.novocliente, name='cliente'),
    
    path('empresas/',funilaria_views.empresa,name='empresa'),
    re_path(r'empresa/(?P<id>\d+)/$',funilaria_views.editar_empresa, name='editar_empresa'),
    re_path(r'empresa/deletar/(?P<id>\d+)/$',funilaria_views.deletar_empresa, name='deletar_empresa'),
    path('empresa/', funilaria_views.novoempresa, name='empresa'),
    url(r'empresa/busca/',empresa,name='busca_empresa'),

    path('ordensdeservico/',funilaria_views.ordem_de_servico,name='ordensdeservico'),
    path('ordemdeservico/', funilaria_views.nova_os, name='ordemdeservico'),
    re_path(r'ordemdeservico/(?P<id>\d+)/$',funilaria_views.editar_os, name='editar_ordem'),
    re_path(r'ordemdeservico/deletar/(?P<id>\d+)/$',funilaria_views.deletar_os, name='deletar_ordem'),
    url(r'ordensdeservico/busca/',ordem_de_servico,name='busca_ordem'),

    path('materiais/',funilaria_views.material,name='material'),
    path('material/', funilaria_views.novo_material, name='material'),
    re_path(r'material/(?P<id>\d+)/$',funilaria_views.editar_material, name='editar_material'),
    re_path(r'material/deletar/(?P<id>\d+)/$',funilaria_views.deletar_material, name='deletar_material'),
    url(r'material/busca/',material,name='busca_material'),

    path('perfil/',usuario_views.perfil_usuario,name='perfil_usuario'),
    path('novo-usuario/',usuario_views.novo_usuario,name='novo_usuario'),
    path('perfil/editar/',usuario_views.editar_usuario,name='formusuario'),
    path('perfil/editar/senha/',usuario_views.alterar_senha,name='alterarsenha'),

    path('login/', usuario_views.login_user),
    path('login/submit', usuario_views.submit_login),
    path('logout/', usuario_views.logout_user),
    re_path(r'add-no-carrinho/(?P<id>\d+)/$', funilaria_views.add_no_carrinho_lista_materiais, name='add_no_carrinho'),
    re_path(r'tirar-do-carrinho/(?P<id>\d+)/$', funilaria_views.tirar_do_carrinho, name='tirar_do_carrinho'),
    re_path(r'add-no-carrinho/#/(?P<id>\d+)/$', funilaria_views.add_no_carrinho_, name='add_no_carrinho2'),
    url(r'add-no-carrinho-editado/(?P<id_material>\d+)-(?P<id_carrinho>\d+)-(?P<orcamento_id>\d+)/$', funilaria_views.add_no_editar_carrinho, name='add_no_editar_carrinho'),
    url(r'tirar-do-carrinho-editado/(?P<id_material>\d+)-(?P<id_carrinho>\d+)-(?P<orcamento_id>\d+)/$', funilaria_views.tirar_do_editar_carrinho, name='tirar_do_editar_carrinho'),
    re_path(r'tirar-do-carrinho/#/(?P<id>\d+)/$', funilaria_views.tirar_do_carrinho_, name='tirar_do_carrinho2'),
    re_path(r'remover-do-carrinho/(?P<id_material>\d+)-(?P<id_carrinho>\d+)/$', funilaria_views.remover_do_carrinho, name='remover_do_carrinho'),
    re_path(r'remover-do-carrinho-editado/(?P<id_material>\d+)-(?P<id_carrinho>\d+)-(?P<orcamento_id>\d+)/$', funilaria_views.remover_do_editar_carrinho, name='remover_do_editar_carrinho'),
    path('carrinho/', carrinho, name='carrinho'),
    re_path(r'carrinho/editar/(?P<id>\d+)-(?P<orcamento_id>\d+)/$', editar_carrinho, name='editar_carrinho'),

    path('orcamentos/',funilaria_views.orcamento,name='orcamentos'),
    path('orcamento/', funilaria_views.novo_orcamento, name='orcamento'),
    re_path(r'orcamento/(?P<id>\d+)/$',funilaria_views.editar_orcamento, name='editar_orcamento'),
    re_path(r'orcamento/(?P<id>\d+)-(?P<carrinho_id>\d+)/$',funilaria_views.editar_orcamento, name='editar_carrinho_do_orcamento'),
    re_path(r'orcamento/deletar/(?P<id>\d+)/$',funilaria_views.deletar_orcamento, name='deletar_orcamento'),
    url(r'orcamento/busca/',orcamento,name='busca_orcamento'),
    path('materiais-os/',funilaria_views.materiais_orcamento,name='materiais_orcamento'),
    path('materiais/',funilaria_views.materiais_orcamento,name='materiais_orcamento'),
    re_path(r'materiais/orcamento/editar/(?P<id_orcamento>\d+)/$',funilaria_views.materiais_orcamento_editar,name='materiais_orcamento_editar'),

    re_path(r'lucros/',funilaria_views.lucros, name='lucros'),
    

    path(r'login/recuperacaodesenha/',usuario_views.senha, name='recuperar_senha'),
    url(r'login/novasenha/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',usuario_views.atribuir_nova_senha, name='password_reset_confirm'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" path('orcamentos/',funilaria_views.orcamento,name='orcamento'),
    path('orcamento/', funilaria_views.novo_orcamento, name='orcamento'),
    re_path(r'orcamento/(?P<id>\d+)/$',funilaria_views.editar_orcamento, name='editar_orcamento'),
    re_path(r'orcamento/deletar/(?P<id>\d+)/$',funilaria_views.deletar_orcamento, name='deletar_orcamento'), """
