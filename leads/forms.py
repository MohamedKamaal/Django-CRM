from django import forms 
from leads.models import Lead, Source, Agent

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"
        
# class LeadForm(forms.Form):
#     first_name = forms.CharField(max_length=20)
#     last_name = forms.CharField(max_length=20)
#     age = forms.IntegerField(min_value=0,max_value=130)
#     phoned = forms.BooleanField(required=False)
#     source = forms.ChoiceField(choices=Source.choices)
#     agent = forms.ModelChoiceField(queryset=Agent.objects.all())
    
