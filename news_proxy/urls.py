from django.urls import path
from .views import NewsList, NewsDetail, NewsEndpointHandler

urlpatterns = [
    path('news/', NewsList.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
    path('news/category/<str:category>/', NewsEndpointHandler.as_view(), {'type': 'category'}, name='news-by-category'),
    path('news/country/<str:country>/', NewsEndpointHandler.as_view(), {'type': 'country'}, name='news-by-country'),
    path('news/source/<str:source>/', NewsEndpointHandler.as_view(), {'type': 'source'}, name='news-by-source'),
    path('news/search/', NewsEndpointHandler.as_view(), {'type': 'search'}, name='news-search'),
]
