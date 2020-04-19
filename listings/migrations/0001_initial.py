# Generated by Django 2.2.9 on 2020-04-16 17:37

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('towns', '0001_initial'),
        ('thumbnails', '0001_initial'),
        ('realtors', '0002_auto_20200411_1128'),
        ('companys', '0005_feature_features_4'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bg_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Border_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Development',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Footer_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hover_border_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hover_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hover_text_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('water', models.CharField(help_text='the distance from water pipe or source', max_length=100, null=True)),
                ('electricity', models.CharField(help_text='distance from the closest transformer', max_length=100, null=True)),
                ('photo_main', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('pytube_video_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('plot_video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
                ('bg_color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Bg_color')),
                ('border_color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Border_color')),
                ('broker', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Broker')),
                ('business', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companys.Business')),
                ('color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Color')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('development', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Development')),
                ('hover_color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Hover_color')),
                ('location', models.ForeignKey(help_text='add a location closet to the plot in the picked town', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='locations.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Neighbor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plot_size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plot_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plot_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Text_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Videolisting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('videofile', models.FileField(null=True, upload_to='videos/')),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('Business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companys.Business')),
                ('broker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Broker')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Listing')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='neighbor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Neighbor'),
        ),
        migrations.AddField(
            model_name='listing',
            name='payment_plan',
            field=models.ForeignKey(help_text='mode of payment required', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Payment_plan'),
        ),
        migrations.AddField(
            model_name='listing',
            name='plot_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Plot_size'),
        ),
        migrations.AddField(
            model_name='listing',
            name='plot_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Plot_status'),
        ),
        migrations.AddField(
            model_name='listing',
            name='plot_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Plot_type'),
        ),
        migrations.AddField(
            model_name='listing',
            name='population',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Population'),
        ),
        migrations.AddField(
            model_name='listing',
            name='roads',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Road'),
        ),
        migrations.AddField(
            model_name='listing',
            name='text_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Text_color'),
        ),
        migrations.AddField(
            model_name='listing',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='thumbnails.Thumbnail'),
        ),
        migrations.AddField(
            model_name='listing',
            name='town',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='towns.Town'),
        ),
    ]
