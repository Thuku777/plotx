# Generated by Django 2.2.9 on 2020-03-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0015_auto_20200318_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='about_pic',
            field=models.ImageField(blank=True, default='panorama.jpg', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='business',
            name='business_pic',
            field=models.ImageField(blank=True, default='panorama.jpg', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to='logos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='business',
            name='service_pic',
            field=models.ImageField(blank=True, default='panorama.jpg', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]