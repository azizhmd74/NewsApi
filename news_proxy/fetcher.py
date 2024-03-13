from requests import get

#news appi key needed to fetch the news and to handle
NEWS_API_KEY = "d34436fbc26b485abe614bf094141cb6"

class NewsFetcher:
    @staticmethod
    #testing via fetching news automtaically from
    def fetch_top_headlines(country='us'):
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"
        response = get(url)
        response.raise_for_status()
        return response.json().get('articles', [])