from django.contrib import admin
from .models import News, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'created_at',
        'published',
    )

    inlines = [
        CommentInline
    ]
    
    search_fields = ('title', 'body')
    list_filter = ('category', 'published')

admin.site.register(News, NewsAdmin)
admin.site.register(Comment)