from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Review, Car
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date, datetime
import re


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label=_("Email"),
        widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}),
        help_text=_("Обязательно. Введите действующий email.")
    )

    phone = forms.CharField(
        required=True,
        max_length=20,
        label=_("Телефон"),
        widget=forms.TextInput(attrs={'placeholder': '+375 (29) XXX-XX-XX'}),
        help_text=_("Формат: +375 (29) XXX-XX-XX")
    )

    birth_date = forms.CharField(
        required=True,
        label=_("Дата рождения"),
        widget=forms.TextInput(attrs={'placeholder': 'DD.MM.YYYY'}),
        help_text=_("Формат: DD.MM.YYYY (Вам должно быть больше 18 лет)")
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone', 'birth_date')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        pattern = r'^\+375\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}$'
        if not re.match(pattern, phone):
            raise ValidationError(_("Номер должен быть в формате: +375 (29) XXX-XX-XX"))
        return phone

    def clean_birth_date(self):
        birth_date_str = self.cleaned_data.get('birth_date')

        try:
            birth_date = datetime.strptime(birth_date_str, '%d.%m.%Y').date()
        except ValueError:
            raise ValidationError(_("Неверный формат даты. Используйте DD.MM.YYYY"))

        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        if age < 18:
            raise ValidationError(_("Вам должно быть больше 18 лет для регистрации."))
        if birth_date > today:
            raise ValidationError(_("Дата рождения не может быть в будущем."))

        return birth_date

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.birth_date = self.cleaned_data['birth_date']
        if commit:
            user.save()
        return user


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'text': 'Ваш отзыв',
            'rating': 'Оценка',
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'price', 'description', 'mileage', 'photo']