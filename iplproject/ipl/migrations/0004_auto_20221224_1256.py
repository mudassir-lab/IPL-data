# Generated by Django 2.2 on 2022-12-24 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0003_auto_20221224_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matches',
            old_name='toss_descision',
            new_name='toss_decision',
        ),
    ]
