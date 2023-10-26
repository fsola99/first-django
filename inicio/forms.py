from django import forms

class CrearPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250) #aunque en el otro dice textfield
    anio = forms.IntegerField()