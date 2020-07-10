from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views import generic
from django import forms
from .models import Banda, Album
from .forms import BandaAdicionarForm, BandaEditarForm, AlbumAdicionarForm


class AdicionarView(generic.edit.FormView):
    template_name = "adicionar_banda.html"
    form_class = BandaAdicionarForm
    success_url = "/bandas/sucesso/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "bandas"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Bandas"
        context["navbar"] = "bandas"
        return context

    def get_queryset(self):
        return Banda.objects.all()


class HomeView(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        # from ipdb import set_trace; set_trace()
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        context["navbar"] = "home"
        return context


class AlbunsView(generic.ListView):
    template_name = "album.html"
    context_object_name = "albuns"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Albuns"
        context["navbar"] = "albuns"
        return context

    def get_queryset(self):
        return Album.objects.all()


class BandaCriadaView(generic.TemplateView):
    template_name = "banda-criada-sucesso.html"


def detail(request, pk):
    banda = Banda.objects.get(pk=pk)
    if banda:
        albuns = Album.objects.filter(banda=banda)
    else:
        albuns = "Não tem album dessa banda"
    return render(
        request, "detail.html", {"banda": banda, "albuns": albuns, "title": "Detalhe"}
    )


def editar_banda(request, pk):
    banda = Banda.objects.get(pk=pk)
    if request.method == "POST":
        form = BandaEditarForm(request.POST)
        if form.is_valid():
            integrantes_banda = form.cleaned_data["integrantes"]
            banda.integrantes = integrantes_banda
            banda.save()
            return redirect("detail", pk=banda.pk)
    form = BandaEditarForm()
    return render(request, "editar.html", {"form": form, "banda": banda})


def apagar_banda(request, pk):
    banda = Banda.objects.get(pk=pk)
    banda.delete()
    return redirect("index")


def criar_albuns(request, pk):
    banda = Banda.objects.get(pk=pk)
    if request.method == "POST":
        form = AlbumAdicionarForm(request.POST)
        if form.is_valid():
            nome_form = form.cleaned_data["nome"]
            ano_lancamento_form = form.cleaned_data["ano_lancamento"]
            Album.objects.create(
                banda=banda, nome=nome_form, ano_lancamento=ano_lancamento_form
            )
            return redirect("detail", pk=banda.pk)
    form = AlbumAdicionarForm()
    return render(request, "adicionar_album.html", {"form": form, "banda": banda})


# def banda_editar(request, pk):
#     banda = Banda.objects.get(pk=pk)
#     if request.method == "POST":
#         form = BandaEditarForm(request.POST)
#         if form.is_valid():
#             integrantes_da_banda = form.cleaned_data['integrantes']
#             banda.integrantes = integrantes_da_banda
#             banda.save()
#             return redirect('detail', pk=banda.pk)
#     form = BandaEditarForm()
#     return render(request, "editar.html", {"form": form})


# def banda_apagar(request, pk):
#     banda = Banda.objects.get(pk=pk)
#     banda.delete()
#     return redirect('index')
