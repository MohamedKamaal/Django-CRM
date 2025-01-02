from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from leads.models import Lead, Agent
from leads.forms import  LeadModelForm
# Create your views here.

def home_page_view(request):
    return render(request, "home.html")


def lead_list_view(request):
    leads = Lead.objects.all()
    context = {"leads":leads}
    return render(request, "leads/lead-list.html",context)

def lead_detail_view(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    context = {"lead":lead}
    return render(request, "leads/lead-detail.html",context) 

def lead_create_view(request):
    form = LeadModelForm()
    
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        print(form)

        if form.is_valid():
            
            form.save()
            
            return redirect("leads:lead-list")
    context = {"form":form}
    return render(request, "leads/lead-create.html", context)

    
def lead_update_view(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(instance=lead, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("leads:lead-detail",lead.pk)   

    context = {"form":form, "lead":lead}
    return render(request, "leads/lead-update.html",context)


def lead_delete_view(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == "POST":
        lead.delete()
        return redirect("leads:lead-list")
    context = {"lead":lead}

    return render(request, "leads/lead-delete.html",context)

def agent_detail_view(request, pk):
    agent = get_object_or_404(Agent, pk=pk)
    context = {"agent":agent}
    return render(request, "leads/agent-detail.html",context) 