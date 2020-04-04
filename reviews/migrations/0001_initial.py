# Generated by Django 2.2.9 on 2020-04-04 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companys', '0030_auto_20200402_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Businessreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200, null=True)),
                ('review', models.TextField(help_text='simple is better than complex', null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('business', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companys.Business')),
            ],
        ),
    ]
