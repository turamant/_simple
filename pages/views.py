from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from pages.models import Rubric, Post,Image


class HomePageView(TemplateView):
    template_name = 'home.html'

class RubricListView(ListView):
    model = Rubric
    template_name = 'pages/rubric_list.html'

class RubricDetailView(DetailView):
    model = Rubric
    template_name = 'pages/rubric_detail.html'
    slug_field = "url"

class RubricCreate(CreateView):
    model = Rubric
    template_name = 'pages/rubric_new.html'
    fields = '__all__'

class RubricUpdate(UpdateView):
    model = Rubric
    slug_field = "url"
    template_name = 'pages/rubric_update.html'
    fields = '__all__'

class RubricDelete(DeleteView):
    model = Rubric
    slug_field = "url"
    template_name = 'pages/rubric_delete.html'
    success_url = reverse_lazy('home')


class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['rubric_list'] = Rubric.objects.all()
        context['image'] = Image.objects.all()
        return context

class PostCreate(CreateView):
    model = Post
    template_name = 'pages/post_new.html'
    fields = '__all__'

class PostUpdate(UpdateView):
    model = Post
    slug_field = "url"
    template_name = 'pages/post_update.html'
    fields = '__all__'

class PostDelete(DeleteView):
    model = Post
    slug_field = "url"
    template_name = 'pages/post_delete.html'
    success_url = reverse_lazy('home')

class AllImageView(ListView):
    model = Image
    template_name = 'pages/all_image.html'



