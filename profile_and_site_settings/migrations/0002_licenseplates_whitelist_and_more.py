# Generated by Django 4.1.7 on 2023-04-19 16:58

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profile_and_site_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicensePlates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=100, verbose_name='Model')),
                ('license_plate', models.CharField(max_length=10, verbose_name='License plate')),
                ('region', django_countries.fields.CountryField(max_length=2, verbose_name='Region')),
            ],
        ),
        migrations.CreateModel(
            name='WhiteList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='User name')),
                ('license_plate', models.CharField(max_length=10, verbose_name='License plate')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='notifications_about_new_features',
            field=models.BooleanField(default=True, verbose_name='Notification about new features'),
        ),
        migrations.AddField(
            model_name='profile',
            name='notifications_when_license_from_white_list_on_photo',
            field=models.BooleanField(default=True, verbose_name='Notification when license plate from "White list" on photo'),
        ),
        migrations.AddField(
            model_name='profile',
            name='notifications_when_my_license_plate_on_photo',
            field=models.BooleanField(default=True, verbose_name='Notification when my license plate on photo'),
        ),
        migrations.AddField(
            model_name='profile',
            name='notifications_when_unfamiliar_license_on_photo',
            field=models.BooleanField(default=True, verbose_name='Notification when unfamiliar license plate on photo'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_license_plate',
            field=models.ManyToManyField(to='profile_and_site_settings.licenseplates', verbose_name='User license plate'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_white_list',
            field=models.ManyToManyField(to='profile_and_site_settings.whitelist', verbose_name='User "White list"'),
        ),
    ]
