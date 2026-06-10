import django.forms as forms
from .models import Team
#importo il mio user personalizzato
from core.models import User

class TeamForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    icon = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)
    members = forms.CharField(widget=forms.HiddenInput(), required=False)  # IDs separati da virgola

    def clean_members(self):
        raw = self.cleaned_data.get('members', '')
        if not raw:
            return []
        try:
            ids = [int(i) for i in raw.split(',') if i.strip()]
        except ValueError:
            raise forms.ValidationError("Dati non validi.")
        if len(ids) > 4:  # max 4 + te stesso = 5
            raise forms.ValidationError("Puoi aggiungere al massimo 4 membri.")
        return User.objects.filter(pk__in=ids, teams__isnull=True)

class ExitTeamForm(forms.Form):
    
    pass
    
