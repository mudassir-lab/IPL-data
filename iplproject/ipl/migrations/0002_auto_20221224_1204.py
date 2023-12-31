# Generated by Django 2.2 on 2022-12-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matches',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='matches',
            name='last_name',
        ),
        migrations.AddField(
            model_name='matches',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='dl_applied',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='palyer_of_match',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='result',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='season',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='team1',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='team2',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='toss_descision',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='toss_winner',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='umpire1',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='umpire2',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='umpire3',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='venue',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='win_by_runs',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='win_by_wickets',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='winner',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
