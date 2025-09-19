from django import forms
from datetime import date, timedelta

class NewsPreferencesForm(forms.Form):
    categories = forms.MultipleChoiceField(
        choices=[(cat['code'], cat['name']) for cat in [
            {'id': 1, 'name': 'Политика', 'code': 'politics'},
            {'id': 2, 'name': 'Технологии', 'code': 'tech'},
            {'id': 3, 'name': 'Спорт', 'code': 'sports'},
            {'id': 4, 'name': 'Экономика', 'code': 'economy'},
            {'id': 5, 'name': 'Культура', 'code': 'culture'},
            {'id': 6, 'name': 'Наука', 'code': 'science'},
        ]],
        widget=forms.CheckboxSelectMultiple,
        label='Выберите категории новостей',
        required=False
    )
    
    language = forms.ChoiceField(
        choices=[('ru', 'Русский'), ('en', 'English'), ('es', 'Español')],
        label='Язык интерфейса'
    )
    
    theme = forms.ChoiceField(
        choices=[('light', 'Светлая'), ('dark', 'Темная')],
        label='Тема оформления'
    )
    
    email_notifications = forms.BooleanField(
        required=False,
        label='Email уведомления'
    )
    
    start_date = forms.DateField(
        required=False,
        label='Новости от даты',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    
    end_date = forms.DateField(
        required=False,
        label='Новости до даты',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Устанавливаем начальные значения для дат, если они не переданы
        if not self.initial.get('start_date'):
            self.initial['start_date'] = date.today() - timedelta(days=7)
        if not self.initial.get('end_date'):
            self.initial['end_date'] = date.today()