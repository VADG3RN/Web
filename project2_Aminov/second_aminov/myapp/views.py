from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
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
    
    # Получаем настройки из cookies
    categories_cookie = request.COOKIES.get('categories', '')
    language_cookie = request.COOKIES.get('language', 'ru')
    theme_cookie = request.COOKIES.get('theme', 'light')
    
    # Преобразуем строку категорий в список
    selected_categories = categories_cookie.split(',') if categories_cookie else []
    
    # Обработка POST запроса (сохранение настроек)
    if request.method == 'POST':
        # Получаем данные из формы
        categories = request.POST.getlist('categories', [])
        language = request.POST.get('language', 'ru')
        theme = request.POST.get('theme', 'light')
        
        # Создаем response с обновленными cookies
        response = redirect('index')
        response.set_cookie('categories', ','.join(categories), max_age=30*24*60*60)
        response.set_cookie('language', language, max_age=30*24*60*60)
        response.set_cookie('theme', theme, max_age=30*24*60*60)
        return response
    
    # Обработка сброса настроек
    if 'reset' in request.GET:
        response = redirect('index')
        response.delete_cookie('categories')
        response.delete_cookie('language')
        response.delete_cookie('theme')
        return response
    
    # Фильтруем новости по выбранным категориям
    if selected_categories and selected_categories != ['']:
        filtered_news = [news for news in news_items if news['category'] in selected_categories]
    else:
        filtered_news = news_items
    
    # Подготавливаем данные для шаблона
    categories_list = [
        {'code': 'politics', 'name_ru': 'Политика', 'name_en': 'Politics'},
        {'code': 'tech', 'name_ru': 'Технологии', 'name_en': 'Technology'},
        {'code': 'sports', 'name_ru': 'Спорт', 'name_en': 'Sports'},
        {'code': 'economy', 'name_ru': 'Экономика', 'name_en': 'Economy'},
        {'code': 'culture', 'name_ru': 'Культура', 'name_en': 'Culture'},
        {'code': 'science', 'name_ru': 'Наука', 'name_en': 'Science'},
    ]
    
    # Проверяем, какие категории выбраны
    for category in categories_list:
        category['checked'] = category['code'] in selected_categories
    
    context = {
        'news_items': filtered_news,
        'categories': categories_list,
        'preferences': {
            'language': language_cookie,
            'theme': theme_cookie,
        },
        'selected_categories': selected_categories,
    }
    
    return render(request, 'myapp/index.html', context)