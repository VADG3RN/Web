from django import forms

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
        required=False
    )
    
    theme = forms.ChoiceField(
        choices=[('light', 'Светлая'), ('dark', 'Темная')],
    )
