# Generated by Django 2.2.9 on 2020-01-17 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20191225_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='location',
        ),
        migrations.RemoveField(
            model_name='company',
            name='town',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='location',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='town',
        ),
        migrations.RemoveField(
            model_name='realtor',
            name='location',
        ),
        migrations.RemoveField(
            model_name='realtor',
            name='town',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Town',
        ),
    ]
