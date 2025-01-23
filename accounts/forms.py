from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # اضافه کردن کلاس‌های CSS به فیلدها
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})