# Generated by Django 2.2.9 on 2020-03-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='church_name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]