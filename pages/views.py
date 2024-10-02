from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import(
    TemplateView,
    CreateView,
    ListView,
    DetailView,
)
from .models import News
from .forms import CommentForm

class HomePageView(TemplateView):
    model = News
    template_name = 'home.html'

class AdminPageView(TemplateView):
    template_name = 'admins_home.html'

class NewsCreateView(CreateView):
    model = News
    template_name = 'news_new.html'
    fields = (
        'title',
        'body',
        'summary',
        'image',
        'category',
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'