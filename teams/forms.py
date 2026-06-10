import django.forms as forms
from .models import Team

class TeamForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False
    )
    icon = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False
    )
    #massimo 5 membri per squadra
    members = forms.ModelMultipleChoiceField(
        queryset=Team.members.field.related_model.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )
    def clean_members(self):
        members = self.cleaned_data['members']
        if len(members) > 5:
            raise forms.ValidationError("Una squadra può avere al massimo 5 membri.")
        return members

class ExitTeamForm(forms.Form):
    
    pass
    
