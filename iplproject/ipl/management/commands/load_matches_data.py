from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from ipl.models import Matches


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the ipldb file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from maches.csv"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if Matches.objects.exists():
            print('matches data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
            
        # Show this before loading the data into the database
        print("Loading maches data")


        #Code to load the data into database
        for match in DictReader(open('/home/mudassir/Mountblue/IPL-in-Django/iplproject/ipl/management/commands/matches.csv')):
            match=Matches(
                id = match['id'],
                city = match['city'],
                date = match['date'],
                dl_applied = match['dl_applied'],
                player_of_match = match['player_of_match'],
                result = match['result'],
                season = match['season'],
                team1 = match['team1'],
                team2 = match['team2'],
                toss_decision = match['toss_decision'],
                toss_winner = match['toss_winner'],
                umpire1 = match['umpire1'],
                umpire2 = match['umpire2'],
                umpire3 = match['umpire3'],
                venue = match['venue'],
                win_by_runs = match['win_by_runs'],
                win_by_wickets = match['win_by_wickets'],
                winner = match['winner']
            )  
            match.save()
            