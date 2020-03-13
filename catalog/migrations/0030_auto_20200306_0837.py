# Generated by Django 2.2.9 on 2020-03-06 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0029_auto_20200306_0818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plot',
            old_name='Plot_status',
            new_name='plot_status',
        ),
        migrations.AlterField(
            model_name='company',
            name='border_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Border_color'),
        ),
        migrations.AlterField(
            model_name='company',
            name='hover_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Hover_color'),
        ),
    ]
