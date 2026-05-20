
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/',views.logout,name='logout'),
    path('recuperar_senha_um/', views.recuperar_senha1, name="recuperar_senha_um"),
    path('recuperar_senha_dois/', views.recuperar_senha2, name="recuperar_senha_dois"),
    path('alterar_senha/<int:id>',views.alterar_senha,name="alterar_senha"),  #type: ignore
    path('dashboard/', views.dashboard, name="dashboard"),
]
