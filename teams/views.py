from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from .forms import TeamForm, ExitTeamForm
from .models import Team
# Create your views here.

class CreateTeamView(FormView):
    template_name = 'teams/create_team.html'
    form_class = TeamForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = self.request.user.teams.first()
        return context

    def form_valid(self, form):
        team = Team.objects.create(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            icon=form.cleaned_data['icon']
        )
        team.members.set(form.cleaned_data['members'])
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