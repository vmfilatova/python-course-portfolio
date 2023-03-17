from django.views.generic import ListView
from django.views.generic import DetailView

from person.models import Person


class PersonListView(ListView):
    model = Person


class PersonDetailView(DetailView):
    model = Person
