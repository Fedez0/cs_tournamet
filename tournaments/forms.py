from .models import Tournament
import django.forms as forms 
class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'date', 'location','prize', 'max_teams']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'prize': forms.TextInput(attrs={'class': 'form-control'}),
            'max_teams': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }
class TournamentSignUpForm(forms.Form):
    # Aggiungi campi specifici per la registrazione al torneo, ad esempio:
    team_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Puoi aggiungere altri campi come membri del team, ecc.
    field_order = ['team_name']  # Ordina i campi come desiderato

