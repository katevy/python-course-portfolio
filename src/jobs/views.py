from django.views.generic import ListView
from django.views.generic import DetailView

from jobs.models import Job


class IndexJobsListView(ListView):
    model = Job


class IndexDetailView(DetailView):
    model = Job
