from binhex import REASONABLY_LARGE
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.db.models import Count, Sum, FloatField, ExpressionWrapper
from .models import Matches, Deliveries


def home_view(request):
    return render(request,'ipl/home.html',{})

def maches_per_year(request):
    data = list(Matches.objects
                .values('season')
                .annotate(match_count=Count('season'))
                .order_by('season')
                )
    return JsonResponse(data, safe=False)


def wins_per_team(request):

    data = list(Matches.objects
                .exclude( winner = '')
                .values('winner', 'season')
                .annotate(wins=Count('winner'))
                .order_by('season','winner')
                )

    return JsonResponse(data, safe=False)


def extra_runs_in_2016(request):
    data = list(Deliveries.objects
                .values('batting_team')
                .filter(match_id__season=2016)
                .annotate(extra_runs=Sum('extra_runs'))
                )

    return JsonResponse(data, safe=False)


def top_bowlers_in_2015(request):
    data = list(Deliveries.objects
                .filter(match_id__season=2015)
                .values('bowler')
                .annotate(econmy=ExpressionWrapper(Sum('total_runs')/(Count('bowler')/6.0), output_field=FloatField()))
                .order_by('econmy')
                )[:10]

    return JsonResponse(data, safe=False)


def chart1(request):
    data = {'main_title': 'Matches Played par Season',
            'x_title': 'Season', 'y_title': 'Matches', 'route':'mpy','x_key': 'season', 'y_key': 'match_count'}
    return render(request, 'ipl/chart1.html', data)


def chart2(request):
    data = {'main_title': 'Wins Per Team Per Season',
            'x_title': 'Team', 'y_title': 'Wins', 'route': 'wpt','x_key': 'winner', 'y_key': 'wins'}
    return render(request, 'ipl/stackedchart.html', data)


def chart3(request):
    data = {'main_title': 'Extra Runs Per Team ', 'x_title': 'Team',
            'y_title': 'Runs', 'route': 'extraruns2016', 'x_key': 'batting_team', 'y_key': 'extra_runs'}
    return render(request, 'ipl/chart1.html', data)

def chart4(request):
    data = {'main_title': 'Top 10 Economical Bowler', 'x_title': 'Bowler',
            'y_title': 'Econmy', 'route': 'topbowlers2015', 'x_key': 'bowler', 'y_key': 'econmy'}
    return render(request, 'ipl/chart1.html', data)


    # Cast(Sum('t')/Count('b'),FloatField())
