from django.core.management.base import BaseCommand
from news_proxy.models import News  
from news_proxy.fetcher import NewsFetcher  # Importing the NewsFetcher class
from datetime import datetime  # Importing datetime module for date and time operations

# # #  management command to fetch news from an external API and save or update them in the database.
# # #  This class inherits from Django's BaseCommand, allowing it to be executed via the Django management
# # #  interface (manage.py). 

class Command(BaseCommand):
    # Help text for the management command
    help = 'Fetches news from an external API and saves or updates them in the database'

    def handle(self, *args, **options):
        # Fetch news from the external API " https://newsapi.org/docs. "
        articles = NewsFetcher.fetch_top_headlines()

        # Save or update each news article in the database
        for article in articles:
            News.objects.update_or_create(
                # Using the title as the unique identifier for updating or creating the news object
                title=article['title'],
                # Providing the default values for fields when creating a new object
                defaults={
                    'description': article['description'],  
                    'url': article['url'], 
                    # Converting the publishedAt string to a datetime object
                    'published_at': datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
                    'content': article.get('content', '')  # Content of the article (if available)
                }
            )
        # Output success message after fetching and saving news
        self.stdout.write(self.style.SUCCESS('News fetched and saved successfully'))
