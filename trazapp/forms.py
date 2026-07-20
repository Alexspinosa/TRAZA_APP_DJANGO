# 
from django import forms


class RegistrarEntradaForm(forms.Form):
    codigo_niif = forms.CharField(
        label="Código NIIF",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Escanee o escriba el código NIIF",
                "autofocus": True,
                "autocomplete": "off",
            }
        ),
    )

    def clean_codigo_niif(self):
        return self.cleaned_data["codigo_niif"].strip().upper()