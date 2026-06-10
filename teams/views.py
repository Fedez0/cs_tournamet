from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from .forms import TeamForm, ExitTeamForm
from .models import Team
from django.http import JsonResponse
from core.models import User
# Create your views here.

def search_users(request):
    query = request.GET.get('q', '')
    users = User.objects.filter(
        username__icontains=query,
        teams__isnull=True
    ).exclude(pk=request.user.pk)[:10]  # escludi te stesso
    
    data = [{'id': u.pk, 'username': u.username} for u in users]
    return JsonResponse(data, safe=False)


class CreateTeamView(FormView):

    template_name = 'teams/create_team.html'

    form_class = TeamForm

    def get_initial(self):

        initial = super().get_initial()

        initial['members'] = [self.request.user]  # creator già selezionato

        return initial

    def form_valid(self, form):
        team = Team.objects.create(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            icon=form.cleaned_data.get('icon')
        )
        members = form.cleaned_data['members']  # già QuerySet
        team.members.set(members)
        team.members.add(self.request.user)  # aggiungi te stesso
        return super().form_valid(form)
    def get_success_url(self):

        return '/'

class TeamListView(TemplateView):
    template_name = 'teams/team_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = self.request.user.teams.first()
        return context
class ExitFromTeamView(FormView):

    template_name = 'teams/exit_team.html'

    form_class = ExitTeamForm

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['team'] = self.request.user.teams.first()

        return context

    def form_valid(self, form):

        team = self.request.user.teams.first()

        if team:

            team.members.remove(self.request.user)

        return super().form_valid(form)

    def get_success_url(self):

        return '/'