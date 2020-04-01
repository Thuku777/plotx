# Generated by Django 2.2.9 on 2020-03-28 01:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20200319_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactchurch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('church', models.CharField(max_length=200)),
                ('church_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('header', models.CharField(blank=True, max_length=300, null=True)),
                ('message', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]