from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'created_at',
        'published',
    )

    search_fields = ('title', 'body')
    list_filter = ('category', 'published')

admin.site.register(News, NewsAdmin)