from .models import MyListing, Contact
from django import forms


class MyListingsForm(forms.ModelForm):
    class Meta:
        model = MyListing
        fields = ['area', 'price', 'location', 'image', 'title', 'listing_type']
        widgets = {
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'listing_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Listing Type'}),
        }
        labels = {
            'area': 'Area',
            'price': 'Price',
            'location': 'Location',
            'image': 'Image',
            'title': 'Title',
            'listing_type': 'Listing Type',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['area'].required = False
        self.fields['location'].required = False


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message', 'car', 'appartements', 'foodandlife', 'shopping', 'travelling']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'message': 'Message',
        }
