from django.urls import path

from jobs.views import IndexJobsListView
from jobs.views import IndexDetailView

urlpatterns = [
    path("", IndexJobsListView.as_view(), name="jobs"),
    path("<int:pk>/", IndexDetailView.as_view(), name="job"),
]
