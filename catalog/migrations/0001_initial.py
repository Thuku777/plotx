# Generated by Django 2.2.9 on 2020-04-21 10:41

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
        ('towns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bg_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Border_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('company_created_on', models.DateField(blank=True, null=True)),
                ('company_slogan', models.CharField(blank=True, max_length=200, null=True)),
                ('company_pic', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')),
                ('logo', models.ImageField(blank=True, default='logo.png', upload_to='logos/%Y/%m/%d/')),
                ('about_company', ckeditor.fields.RichTextField(help_text='Max 200 words', max_length=1500, null=True)),
                ('about_pic', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')),
                ('service_pic', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')),
                ('services', ckeditor.fields.RichTextField(help_text='Max 200 words', max_length=1500, null=True)),
                ('contact_person', models.CharField(max_length=100, null=True)),
                ('email_1', models.CharField(blank=True, max_length=100, null=True)),
                ('email_2', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_1', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_2', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('Instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
                ('bg_color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Bg_color')),
                ('border_color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Border_color')),
                ('color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Color')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['company_name', 'contact_person', 'phone_1'],
            },
        ),
        migrations.CreateModel(
            name='Development',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Footer_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hover_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('price', models.IntegerField()),
                ('water', models.CharField(help_text='the distance from water pipe or source', max_length=100, null=True)),
                ('electricity', models.CharField(help_text='distance from the closest transformer', max_length=100)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('bg_color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Bg_color')),
                ('border_color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Border_color')),
                ('color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Color')),
                ('company', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Company')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('development', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Development')),
                ('hover_color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Hover_color')),
                ('location', models.ForeignKey(help_text='add a location closet to the plot in the picked town', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='locations.Location')),
                ('neighbor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Neighbor')),
                ('payment_plan', models.ForeignKey(help_text='mode of payment required', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Payment_plan')),
            ],
            options={
                'ordering': ['list_date'],
            },
        ),
        migrations.CreateModel(
            name='Plot_size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plot_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plot_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Text_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('profile', models.ImageField(blank=True, default='avatar.jpg', upload_to='profiles/%Y/%m/%d/')),
                ('statement', models.CharField(blank=True, max_length=400, null=True)),
                ('about_realtor', models.TextField(help_text='Enter a brief description of the Realtor.', max_length=1000)),
                ('advert_pic', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')),
                ('about_pic', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ManyToManyField(blank=True, help_text='Select The  Locations where this realtor  is found in the choosen Town', to='locations.Location')),
                ('town', models.ManyToManyField(blank=True, help_text='Select the towns where this realtor is found', to='towns.Town')),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'phone'],
            },
        ),
        migrations.CreateModel(
            name='PlotInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular plot in the system', primary_key=True, serialize=False)),
                ('plot_number', models.CharField(blank=True, max_length=200, null=True)),
                ('next_payment_due_when', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('s', 'Sold'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved'), ('m', 'Maintenance')], default='a', help_text='plot availability', max_length=1)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('plot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Plot')),
            ],
            options={
                'ordering': ['next_payment_due_when'],
                'permissions': (('can_mark_paid', 'Set plot as paid'),),
            },
        ),
        migrations.AddField(
            model_name='plot',
            name='plot_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Plot_size'),
        ),
        migrations.AddField(
            model_name='plot',
            name='plot_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Plot_status'),
        ),
        migrations.AddField(
            model_name='plot',
            name='plot_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Plot_type'),
        ),
        migrations.AddField(
            model_name='plot',
            name='population',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Population'),
        ),
        migrations.AddField(
            model_name='plot',
            name='realtor',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Realtor'),
        ),
        migrations.AddField(
            model_name='plot',
            name='roads',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Road'),
        ),
        migrations.AddField(
            model_name='plot',
            name='text_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Text_color'),
        ),
        migrations.AddField(
            model_name='plot',
            name='town',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='towns.Town'),
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('mobile', models.CharField(max_length=100)),
                ('header', models.CharField(blank=True, max_length=400, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved_contactus', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='catalog.Company')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AddField(
            model_name='company',
            name='footer_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Footer_color'),
        ),
        migrations.AddField(
            model_name='company',
            name='hover_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Hover_color'),
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.ManyToManyField(blank=True, help_text='Select The exact locations where this Company  is found in the choosen Town', to='locations.Location'),
        ),
        migrations.AddField(
            model_name='company',
            name='realtor',
            field=models.ManyToManyField(blank=True, help_text='realtors', to='catalog.Realtor'),
        ),
        migrations.AddField(
            model_name='company',
            name='text_color',
            field=models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Text_color'),
        ),
        migrations.AddField(
            model_name='company',
            name='town',
            field=models.ManyToManyField(blank=True, help_text='Select The exact towns this company is located.', to='towns.Town'),
        ),
    ]
