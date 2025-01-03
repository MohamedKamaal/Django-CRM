from django.urls import path

app_name = "leads"
from leads.views import *

urlpatterns = [
    path("",LeadListView.as_view(), name="lead-list"),
    path("create/",LeadCreateView.as_view(), name="lead-create"),
    path("<int:pk>/",LeadDetailView.as_view(), name="lead-detail"),
    path("<int:pk>/update/",LeadUpdateView.as_view(), name="lead-update"),
    path("<int:pk>/delete/",LeadDeleteView.as_view(), name="lead-delete"),
]