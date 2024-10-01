from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import News

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
