from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from leads.models import Lead, Agent
from leads.forms import  LeadModelForm, CustomUserCreationForm
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from django.core.mail import send_mail
# Create your views here.

""" function view

def lead_delete_view(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == "POST":
        lead.delete()
        return redirect("leads:lead-list")
    context = {"lead":lead}

    return render(request, "leads/lead-delete.html",context)
function view
def home_page_view(request):
    return render(request, "home.html")

class View

# function view
def lead_detail_view(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    context = {"lead":lead}
    return render(request, "leads/lead-detail.html",context) 



function view

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

function view

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
function view
def lead_list_view(request):
    leads = Lead.objects.all()
    context = {"leads":leads}
    return render(request, "leads/lead-list.html",context) """



# ------------------------------------------------------

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    def get_success_url(self):
        return reverse("login")
    

class HomePageView(TemplateView):
    template_name = "home.html"
    

class LeadListView(ListView):
    template_name = "leads/lead-list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"
    
    
class LeadDetailView(DeleteView):
    template_name = "leads/lead-detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(CreateView):
    template_name = "leads/lead-create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        # send email
        send_mail("A lead has been created","Go to site to see new lead ",from_email="test@gmail.com",recipient_list=['test@yahoo.com'])
        return super().form_valid(form)
    

class LeadUpdateView(UpdateView):
    template_name = "leads/lead-update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    context_object_name = "lead"
    
    def get_success_url(self):
        return reverse("leads:lead-detail",kwargs={"pk":self.object.pk})


class LeadDeleteView(DeleteView):
    template_name = "leads/lead-delete.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"
    
    def get_success_url(self):
        return reverse("leads:lead-list")