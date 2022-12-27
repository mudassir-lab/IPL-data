from django.urls import path

from . import views

app_name = 'ipl'
urlpatterns = [
    path('', views.home_view),
    path('mpy/', views.maches_per_year, name='mpy'),
    path('wpt/', views.wins_per_team, name='wpt'),
    path('extraruns2016/', views.extra_runs_in_2016, name='extraruns2016'),
    path('topbowlers2015/', views.top_bowlers_in_2015, name='topbowlers2015'),

    path('mpychart/', views.chart1, name='mpychart'),
    path('2/', views.chart2, name='wptchart'),
    path('extraruns2016chart/', views.chart3, name='extraruns2016chart'),
    path('topbwlers2015chart/', views.chart4, name='topbowlers2015chart'),
]
