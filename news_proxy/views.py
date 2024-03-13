from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
from django.http import JsonResponse
from .models import News
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer


#retrieving the list of articles and sorting/filtering them the way we want
class NewsList(APIView):
    def get(self, request, format=None):
        # Get query parameters
        category = request.GET.get('category', None)
        source = request.GET.get('source', None)
        query = request.GET.get('query', None)

        # Filter articles based on query parameters
        articles = News.objects.all()

        if category:
            articles = articles.filter(category=category)
        if source:
            articles = articles.filter(source=source)
        if query:
            articles = articles.filter(title__icontains=query)

        # Serialize articles and return response
        serializer = NewsSerializer(articles, many=True)
        return Response(serializer.data) 
    
# Handles different types of news-related API views (e.g., category, country, source, search).
class NewsEndpointHandler(View):
    def get(self, request, *args, **kwargs):
        # Determine the type of request (category, country, source, or search)
        request_type = kwargs.get('type')

        if request_type == 'category':
            return self.get_news_by_category(request, *args, **kwargs)
        elif request_type == 'country':
            return self.get_news_by_country(request, *args, **kwargs)
        elif request_type == 'source':
            return self.get_news_by_source(request, *args, **kwargs)
        elif request_type == 'search':
            return self.search_news(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Invalid request type'}, status=400)

    def get_news_by_category(self, request, category, *args, **kwargs):
        # Get news by category
        news = News.objects.filter(category=category)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def get_news_by_country(self, request, country, *args, **kwargs):
        # Get news by country
        news = News.objects.filter(country=country)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def get_news_by_source(self, request, source, *args, **kwargs):
        # Get news by source
        news = News.objects.filter(source=source)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def search_news(self, request, *args, **kwargs):
        # Search news by title query
        query = request.GET.get('q', '')
        news = News.objects.filter(title__icontains=query)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
    


# # this class handles the detail view of a single news article we chose .
class NewsDetail(APIView):
    def get(self, request, pk, format=None):
        news = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

