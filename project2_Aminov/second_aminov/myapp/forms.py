from django import forms
from django.core.exceptions import ValidationError
import re

class PasswordForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль")

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("Длина пароля должна быть не менее 8 символов.")
        if not re.search(r'[A-Z]', password1):
            raise ValidationError("Пароль должен содержать хотя бы одну прописную букву.")
        if not re.search(r'\d', password1):
            raise ValidationError("Пароль должен содержать хотя бы одну цифру.")
        if not re.search(r'[a-zA-Z]', password1):
            raise ValidationError("Пароль должен содержать только символы латинского алфавита.")
        if not re.search(r'[&#?]', password1):
            raise ValidationError("Пароль должен содержать хотя бы один из символов: #&?")
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли должны совпадать.")
