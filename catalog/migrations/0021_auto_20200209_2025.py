# Generated by Django 2.2.9 on 2020-02-09 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_realtor_realtor_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='realtor_pic',
            new_name='advert_pic',
        ),
    ]
