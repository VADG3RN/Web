from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewsPreferencesForm
import json
from datetime import datetime, timedelta
from django.utils import timezone

def index(request):
    # Обработка сброса настроек
    if request.method == 'POST' and 'reset' in request.POST:
        response = redirect('index')
        response.delete_cookie('news_preferences')
        return response
    
    # Получаем настройки из cookies
    preferences_str = request.COOKIES.get('news_preferences', '{}')
    try:
        preferences = json.loads(preferences_str)
    except json.JSONDecodeError:
        preferences = {}
    
    # Устанавливаем начальные значения по умолчанию
    default_preferences = {
        'categories': [],
        'theme': 'light',
    }
    
    # Объединяем с настройками по умолчанию
    for key, value in default_preferences.items():
        preferences[key] = preferences.get(key, value)
    
    # Создаем форму с текущими настройками
    form_initial = {
        'categories': preferences.get('categories', []),
        'theme': preferences.get('theme', 'light'),
    }
    
    form = NewsPreferencesForm(initial=form_initial)
    
    if request.method == 'POST' and 'reset' not in request.POST:
        form = NewsPreferencesForm(request.POST)
        if form.is_valid():
            # Сохраняем настройки в cookies
            response = redirect('index')
            preferences = {
                'categories': form.cleaned_data['categories'],
                'theme': form.cleaned_data['theme'],
            }
            response.set_cookie('news_preferences', json.dumps(preferences), max_age=30*24*60*60)
            return response
    
    # Данные новостей
    news_items = [
        {
            'id': 1,
            'title': 'Важные политические события в мире', 
            'category': 'politics', 
            'date': '2025-01-15',
            'image': 'politics-news.jpg',
            'content': 'Международные переговоры привели к важным соглашениям между странами.'
        },
        {
            'id': 2,
            'title': 'Новые технологии в IT индустрии', 
            'category': 'tech', 
            'date': '2025-01-14',
            'image': 'technology-news.jpg',
            'content': 'Компания Apple представила новый революционный продукт.'
        },
        {
            'id': 3,
            'title': 'Спортивные достижения сборной', 
            'category': 'sports', 
            'date': '2025-01-13',
            'image': 'sports-news.jpg',
            'content': 'Наши спортсмены завоевали золотые медали на чемпионате мира.'
        },
        {
            'id': 4,
            'title': 'Экономические реформы', 
            'category': 'economy', 
            'date': '2025-01-12',
            'image': 'economy-news.jpg',
            'content': 'Правительство объявило о новых мерах поддержки бизнеса.'
        },
        {
            'id': 5,
            'title': 'Культурные события недели', 
            'category': 'culture', 
            'date': '2025-01-11',
            'image': 'culture-news.jpg', 
            'content': 'В столице открылась новая выставка современного искусства.'
        },
        {
            'id': 6,
            'title': 'Научные открытия года', 
            'category': 'science', 
            'date': '2025-01-10',
            'image': 'science-news.jpg',
            'content': 'Ученые сделали прорыв в области квантовых вычислений.'
        }
    ]
    
    selected_categories = preferences.get('categories', [])
    if not selected_categories:
        filtered_news = news_items
    else:
        filtered_news = [news for news in news_items if news['category'] in selected_categories]
    
    context = {
        'form': form,
        'news_items': filtered_news,
        'preferences': preferences,
    }
    return render(request, 'myapp/index.html', context)

def save_visited_page(request, page_name):
    visited_pages = request.COOKIES.get('visited_pages', '[]')
    try:
        visited_pages = json.loads(visited_pages)
    except json.JSONDecodeError:
        visited_pages = []
    
    if page_name not in visited_pages:
        visited_pages.append(page_name)
        if len(visited_pages) > 5:
            visited_pages = visited_pages[-5:]
    
    response = HttpResponse(f"Страница {page_name} посещена")
    response.set_cookie('visited_pages', json.dumps(visited_pages), max_age=30*24*60*60)
    return response