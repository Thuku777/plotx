# Generated by Django 2.2.9 on 2020-03-31 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0023_auto_20200331_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='company_created_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]