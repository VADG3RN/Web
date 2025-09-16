from django.urls import path
from .views import home_page_view, password_view

urlpatterns = [
    path('', home_page_view, name='home'),
    path('password/', password_view, name='password_view'),
]