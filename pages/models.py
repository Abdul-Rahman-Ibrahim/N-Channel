from django.db import models
from django.urls import reverse
from django.conf import settings

class News(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, null=True, blank=True)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    image = models.ImageField(upload_to='news_images/', blank=True, null=True)

    CATEGORY_CHOICES = (
        ('NEWS', 'News'),
        ('POLITICS', 'Politics'),
        ('ELECTION', 'Election'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('SPORTS', 'Sports'),
        ('HEALTH', 'Health'),
        ('BUSINESS', 'Business'),
        ('LIVE', 'Live'),
    )

    category = models.CharField(
        max_length=15,
        choices=CATEGORY_CHOICES,
        default='NEWS',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})