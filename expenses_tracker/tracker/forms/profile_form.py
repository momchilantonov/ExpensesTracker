from django import forms
from expenses_tracker.tracker.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Last Name',
                }
            ),
            'budget': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Budget",
                }
            )
        }
