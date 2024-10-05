from django.urls import path
from .views import (HomePageView, 
                    AdminPageView, 
                    NewsCreateView,
                    NewsListView,
                    NewsDetailView,
                    PoliticsListView,
                    ElectionListView,
                    EntertainmentListView,
                    SportsListView,
                    HealthListView,
                    BusinessListView,
                    LiveView,
)

urlpatterns = [
    path('live/', LiveView.as_view(), name='live'),
    path('business/', BusinessListView.as_view(), name='business_list'),
    path('health/', HealthListView.as_view(), name='health_list'),
    path('sports/', SportsListView.as_view(), name='sports_list'),
    path('entertainment/', EntertainmentListView.as_view(), name='entertainment_list'),
    path('election/', ElectionListView.as_view(), name='election_list'),
    path('politics/', PoliticsListView.as_view(), name='politics_list'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('administrator/new', NewsCreateView.as_view(), name='news_new'),
    path('administrator/', AdminPageView.as_view(), name='admins_home'),
    path('', HomePageView.as_view(), name='home'),
]