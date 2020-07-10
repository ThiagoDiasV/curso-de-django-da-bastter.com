from django.contrib import admin
from django.urls import path
from bandas import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("bandas/", views.IndexView.as_view(), name="index"),
    path("albuns/", views.AlbunsView.as_view(), name="albuns"),
    path("bandas/<int:pk>", views.detail, name="detail"),
    path("bandas/adicionar/", views.AdicionarView.as_view(), name="adicionar"),
    path("bandas/sucesso/", views.BandaCriadaView.as_view(), name="sucesso"),
    path("bandas/editar/<int:pk>", views.editar_banda, name="editar"),
    path("bandas/apagar/<int:pk>", views.apagar_banda, name="apagar"),
    path("bandas/adicionar-album/<int:pk>", views.criar_albuns, name="criar_album"),
]



