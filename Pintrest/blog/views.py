from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.


def home(request):
    context = {
        'posts': Photo.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Photo
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Photo


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
