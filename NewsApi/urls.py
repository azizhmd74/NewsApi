from django.contrib import admin
from django.urls import path, include  # Include for app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('news_proxy.urls')),  # Include URLs from news_proxy app
    # Other URL patterns for your project (if any)
]
