from django import forms
from expenses_tracker.tracker.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Title",
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'class': 'form_control',
                    'placeholder': "Enter Img URL",
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Description",
                    'rows': 3,
                    'style': 'resize:none',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Price',
                }
            )
        }
