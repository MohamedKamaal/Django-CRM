from django.urls import path

app_name = "leads"
from leads.views import *

urlpatterns = [
    path("",lead_list_view, name="lead-list"),
    path("create/",lead_create_view, name="lead-create"),
    path("<int:pk>/",lead_detail_view, name="lead-detail"),
    path("<int:pk>/update/",lead_update_view, name="lead-update"),
    path("<int:pk>/delete/",lead_delete_view, name="lead-delete"),
    path("agents/<int:pk>/",agent_detail_view, name="agent-detail"),
]