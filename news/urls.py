from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
from django.contrib.auth import login, logout



urlpatterns = [
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('', cache_page(60)(HomeNews.as_view()), name='home'), # Вариант с кэшированием главной страницы
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'Заголовок для категорий'}),
         name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('pages/', pagination, name='pages'),



# urlpatterns без кэширования 'home'
# urlpatterns = [
#     path('contact/', contact, name='contact'),
#     path('register/', register, name='register'),
#     path('login/', user_login, name='login'),
#     path('logout/', user_logout, name='logout'),
#     # path('', index, name='home'),
#     path('', HomeNews.as_view(), name='home'),
#     # path('category/<int:category_id>/', get_category, name='category'),
#     path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'Заголовок для категорий'}),
#          name='category'),
#     # path('news/<int:news_id>/', view_news, name='view_news'),
#     path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
#     # path('news/add-news/', add_news, name='add_news'),
#     path('news/add-news/', CreateNews.as_view(), name='add_news'),
#     path('pages/', pagination, name='pages'),
]
