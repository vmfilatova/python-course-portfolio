from django.views.generic import ListView

from jobs.models import Job


class IndexJobsListView(ListView):
    model = Job
