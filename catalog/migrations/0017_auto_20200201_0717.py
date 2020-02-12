# Generated by Django 2.2.9 on 2020-02-01 04:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20200122_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='service_pic',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='company',
            name='services',
            field=ckeditor.fields.RichTextField(help_text='Max 200 words', max_length=1500, null=True),
        ),
    ]