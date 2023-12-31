from django.db import models

# Create your models here.


class Matches(models.Model):

    id = models.IntegerField(primary_key=True)
    season = models.IntegerField(null=True)
    city = models.CharField(max_length=20, null=True)
    date = models.DateField(null=True)
    team1 = models.CharField(max_length=40, null=True)
    team2 = models.CharField(max_length=40, null=True)
    toss_winner = models.CharField(max_length=40, null=True)
    toss_decision = models.CharField(max_length=40, null=True)
    result = models.CharField(max_length=10, null=True)
    dl_applied = models.IntegerField(null=True)
    winner = models.CharField(max_length=40, null=True)
    win_by_runs = models.IntegerField(null=True)
    win_by_wickets = models.IntegerField(null=True)
    player_of_match = models.CharField(max_length=30, null=True)
    venue = models.CharField(max_length=80, null=True)
    umpire1 = models.CharField(max_length=40, null=True)
    umpire2 = models.CharField(max_length=40, null=True)
    umpire3 = models.CharField(max_length=40, null=True)


class Deliveries(models.Model):

    match_id = models.ForeignKey(Matches, on_delete=models.CASCADE)
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=100)
    bowling_team = models.CharField(max_length=100)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=100)
    non_striker = models.CharField(max_length=100)
    bowler = models.CharField(max_length=100)
    is_super_over = models.IntegerField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=100)
    dismissal_kind = models.CharField(max_length=100)
    fielder = models.CharField(max_length=100)
