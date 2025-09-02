from dashboard.views import book_list
from django.urls import path
from .views import home , about ,query_list , query_details

app_name = 'dashboard'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about , name='about'),

    path('queries/', query_list , name='query_list'),
    path('queries/<slug:slug>/', query_details , name='query_details'),

    path('books/', book_list , name='book_list'),
]