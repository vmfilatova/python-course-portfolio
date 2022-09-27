from django.views.generic import ListView
from django.views.generic import DetailView

from blog.models import Blog


class BlogsListView(ListView):
    model = Blog


class BlogsDetailView(DetailView):
    model = Blog
