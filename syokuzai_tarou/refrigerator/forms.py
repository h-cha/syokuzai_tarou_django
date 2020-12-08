from django import forms
from .models import *
from .models import Food
from . import models
from django.contrib.admin import widgets
import bootstrap_datepicker_plus as datetimepicker
import os



#radio
class SelectForm(forms.Form): 
    select = forms.ModelChoiceField(
        models.Food.objects,
        label=Food.foodName,
        widget=forms.RadioSelect, 
        initial=0
        )

#checkbox
class CheckForm(forms.Form):
    delete = forms.ModelChoiceField(
        models.Food.objects,
        label=Food.foodName,
        widget=forms.CheckboxInput,
        initial=0
    )

class FoodsForm(forms.Form):
    def __init__(self,foodName, foods=[],*args,**kwargs ):
        super(FoodsForm, self).__init__(*args,**kwargs)
        self.fields['foods'] = forms.MultipleChoiceField(
            choices = [(item.foodName,item.foodName) for item in foods],
            widget = forms.CheckboxSelectMultiple(),
            initial = 0
        )

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['foodName']

class FoodSetForm(forms.ModelForm):
    class Meta:
        model = FoodSet
        
        fields = ['food','limitRegister','foodGram']
        widgets = {
            'limitRegister': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }