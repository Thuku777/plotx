# Generated by Django 2.2.9 on 2020-03-29 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('churches', '0010_auto_20200329_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sermon',
            name='Video',
        ),
        migrations.AddField(
            model_name='church_choir',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='churches.Video'),
        ),
        migrations.AddField(
            model_name='sermon',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='churches.Video'),
        ),
        migrations.AddField(
            model_name='weekly_theme',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='churches.Video'),
        ),
    ]