from django.urls import path
from .views import index_view, chat_view, default_view, sidebar_view

urlpatterns = [
    path('', index_view, name='index'),
    path('chat/', chat_view, name='chat'),
    path('default/', default_view, name='default'),
    path('components/sidebar/', sidebar_view, name='sidebar'),
    path('pages/chat/<int:user_id>/', chat_view, name='chat_page'),
    path('pages/default/', default_view, name='default_page'),
]