from re import U

from django.urls import path
from . import views 

urlpatterns = [
    path('livros/', views.livros, name='livros'),
    path('add-categorias/', views.add_categorias, name='add_categorias'),
]