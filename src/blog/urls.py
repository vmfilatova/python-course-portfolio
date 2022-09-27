from django.urls import path

from blog.views import BlogsListView
from blog.views import BlogsDetailView

urlpatterns = [
    path("", BlogsListView.as_view(), name="blogs"),
    path("<int:pk>/", BlogsDetailView.as_view(), name="blog"),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
