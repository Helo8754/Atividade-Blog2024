from django.urls import path

from .views import (
    cadastrar_noticia,
    listar_categoria,
    cadastrar_categoria,
    editar_categoria,
    excluir_categoria,
    editar_noticia,
    inicio_gerencia,
    listagem_noticia,
)

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    # Add your URL patterns here
    path('categorias/', listar_categoria, name='listar_categoria'),
    path('categorias/cadastro', cadastrar_categoria, name='cadastrar_categoria'),
    path('categorias/editar/<int:id>', editar_categoria, name='editar_categoria'),
    path('categorias/excluir/<int:id>', excluir_categoria, name='excluir_categoria')
]