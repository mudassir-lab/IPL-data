from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from ipl.models import Matches,Deliveries


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the ipldb file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from deliveries.csv"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if Deliveries.objects.exists():
            print(' deliveries data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
            
        # Show this before loading the data into the database
        print("Loading deliveries data")


        #Code to load the data into database
        for delivery in DictReader(open('/home/mudassir/Mountblue/IPL-in-Django/iplproject/ipl/management/commands/deliveries.csv')):
            delivery = Deliveries(
                match_id_id=delivery['match_id'],
                inning = delivery['inning'],
                batting_team =delivery['batting_team'] ,
                bowling_team = delivery['bowling_team'],
                over = delivery['over'],
                ball = delivery['ball'],
                batsman = delivery['batsman'],
                non_striker = delivery['non_striker'],
                bowler = delivery['bowler'],
                is_super_over = delivery['is_super_over'],
                wide_runs = delivery['wide_runs'],
                bye_runs = delivery['bye_runs'],
                legbye_runs = delivery['legbye_runs'],
                noball_runs = delivery['noball_runs'],
                penalty_runs = delivery['penalty_runs'],
                batsman_runs = delivery['batsman_runs'],
                extra_runs = delivery['extra_runs'],
                total_runs = delivery['total_runs'],
                player_dismissed = delivery['player_dismissed'],
                dismissal_kind = delivery['dismissal_kind'],
                fielder =   delivery['fielder'],

            )  
            delivery.save()
            