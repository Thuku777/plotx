# Generated by Django 2.2.9 on 2020-04-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('companys', '0005_feature_features_4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='location',
        ),
        migrations.AddField(
            model_name='business',
            name='location',
            field=models.ManyToManyField(blank=True, help_text='Select The exact locations where this Company  is found in the choosen Town', to='locations.Location'),
        ),
    ]
