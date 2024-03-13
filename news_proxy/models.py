from django.db import models

class News(models.Model): 
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    published_at = models.DateTimeField()
    content = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, null=True, blank=True) 

    def __str__(self):
        return self.title
