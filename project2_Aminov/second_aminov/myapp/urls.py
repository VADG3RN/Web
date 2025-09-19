from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('visited/<str:page_name>/', views.save_visited_page, name='save_visited_page'),
]