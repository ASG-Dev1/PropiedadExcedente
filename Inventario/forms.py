from os import link
from django import forms
from django.forms import ModelForm
from .models import Auto
from .models import Articulo
from django.forms import ClearableFileInput

#create a Subasta Form





class AutoForm(ModelForm):
    class Meta:
        
        model = Auto
        fields = ('vin','marca','modelo','year','tablilla','color',
        'cantidad', 'condicion', 'localizacion', 'archivo')
    
     
        labels = {
            'vin':'Vin Number:' , 
            'marca': 'Marca:',
            'modelo': 'Modelo:',
            'year':'Año:',
            'tablilla':'Tablilla:',
            'color':'Color:',
            'cantidad':'Cantidad:',
            'condicion':'Condición:',
            'localizacion':'Localización:',
            'archivo':'Archivo:'
        }
        widgets = {
            'vin': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte Vin Number.', 'width':'10px','style':'margin-top:10px'}), 
            'marca':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte marca.', 'width':'10px','style':'margin-top:10px'}) ,
            'modelo':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte modelo.', 'width':'10px','style':'margin-top:10px'}),
            'year': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte año.', 'width':'10px','style':'margin-top:10px'}),
            'tablilla':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte numero de tablilla.', 'width':'10px','style':'margin-top:10px'}), 
            'color':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte color.', 'width':'10px','style':'margin-top:10px'}), 
            'cantidad':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte cantidad.', 'width':'10px','style':'margin-top:10px'}), 
            'condicion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte condición.', 'width':'10px','style':'margin-top:10px'}), 
            'localizacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte localización.', 'width':'10px','style':'margin-top:10px'}), 
            'archivo': forms.ClearableFileInput(attrs={'class':'form-control','type':'file','id':'formFile', 'placeholder':'Seleccione imagen', 'multiple':False ,'style':'margin-top:10px' }),

      
        }

class ArticuloForm(ModelForm):
    class Meta:
        
        model = Articulo
        fields = ('nombrearticulo','descripcion','cantidad','condicion','localizacion', 'archivo')
    
     
        labels = {
            'nombrearticulo': 'Nombre Articulo:',
            'descripcion': 'Descripción:',
            'cantidad':'Cantidad:',
            'condicion':'Condición:',
            'localizacion':'Localización:',
            'archivo':'Archivo:'
        }
        widgets = {
            'nombrearticulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte nombre de Artículo','style':'margin-top:10px'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte descripción.','style':'margin-top:10px'}),
            'cantidad':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte cantidad.','style':'margin-top:10px'}),
            'condicion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte condición.','style':'margin-top:10px'}),
            'localizacion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Inserte localización.','style':'margin-top:10px'}),
            'archivo': forms.ClearableFileInput(attrs={'class':'form-control','type':'file','id':'formFile', 'placeholder':'Seleccione imagen', 'multiple':False ,'style':'margin-top:10px' }),

            
        }     
