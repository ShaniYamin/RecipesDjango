from django import forms
# from .models import Recipe,Quantity
from django.forms import inlineformset_factory

# class QuantityForm(forms.ModelForm):
#     class Meta:
#         model = Quantity
#         fields = ['ingredient', 'quantity']
#         widgets = {
#             'ingredient': forms.TextInput(),
#             'quantity': forms.TextInput(),
#         }
        

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['ingredient'].widget.attrs.update({'rows': 1})
#         self.fields['quantity'].widget.attrs.update({'rows': 1})
        
# class CreateRecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = "__all__"
#         widgets = {
#             'instructions': forms.Textarea(attrs={'rows': 4}),
#             'tips': forms.Textarea(attrs={'rows': 4}),
#         }
#     QuantityFormSet = inlineformset_factory(Recipe, Quantity, form=QuantityForm, extra=1, can_delete=False)
    
#     quantity_formset = QuantityFormSet()