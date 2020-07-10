from django import forms
from .models import Banda, Album


class BandaAdicionarForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = "__all__"


class BandaEditarForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ["integrantes"]


class AlbumAdicionarForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["nome", "ano_lancamento"]
