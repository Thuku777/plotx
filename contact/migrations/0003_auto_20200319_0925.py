# Generated by Django 2.2.9 on 2020-03-19 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='company',
            new_name='business',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='company_id',
            new_name='business_id',
        ),
    ]