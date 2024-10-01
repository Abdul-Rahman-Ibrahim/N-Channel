from django.urls import path
from .views import HomePageView, AdminPageView, NewsCreateView

urlpatterns = [
    path('administrator/<int:pk>/', NewsCreateView.as_view(), name='news_detail'),
    path('administrator/new', NewsCreateView.as_view(), name='news_new'),
    path('administrator/', AdminPageView.as_view(), name='admins_home'),
    path('', HomePageView.as_view(), name='home'),
]