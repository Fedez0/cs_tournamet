from django.urls import path
from .views import (
    CreateTeamView,
    TeamListView,
    ExitFromTeamView
)
urlpatterns = [
    path('create/', CreateTeamView.as_view(), name='create_team'),
    path('list/', TeamListView.as_view(), name='team_list'),
    path('exit/', ExitFromTeamView.as_view(), name='exit_team'),
]
