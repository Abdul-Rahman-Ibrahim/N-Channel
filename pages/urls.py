from django.urls import path
from .views import (HomePageView, 
                    AdminPageView, 
                    NewsCreateView,
                    NewsListView,
                    NewsDetailView,
                    PoliticsListView
)

urlpatterns = [
    path('politics/', PoliticsListView.as_view(), name='politics_list'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('administrator/new', NewsCreateView.as_view(), name='news_new'),
    path('administrator/', AdminPageView.as_view(), name='admins_home'),
    path('', HomePageView.as_view(), name='home'),
]