from django.views.generic import(
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    FormView,
)
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse

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
        'published',
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class NewsDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
    
class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'

class PoliticsListView(ListView):
    model = News
    template_name = 'politics_list.html'
    context_object_name = 'politics_list'
    

class CommentGet(DetailView):
    model = News
    template_name = 'news_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class CommentPost(SingleObjectMixin, FormView):
    model = News
    form_class = CommentForm
    template_name = 'news_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.news = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        news = self.get_object()
        return reverse('news_detail', kwargs={'pk': news.pk})