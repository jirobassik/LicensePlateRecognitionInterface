# Generated by Django 4.1.7 on 2023-05-10 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_and_site_settings', '0004_rename_licenseplate_licenseplatelist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='licenseplatelist',
            options={'verbose_name': 'License plate list', 'verbose_name_plural': 'License plate lists'},
        ),
        migrations.AlterModelOptions(
            name='whitelist',
            options={'verbose_name': 'White list', 'verbose_name_plural': 'White lists'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.AlterField(
            model_name='profile',
            name='notifications_about_new_features',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Notification about new features'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='notifications_when_license_from_white_list_on_photo',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Notification when license plate from "White list" on photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='notifications_when_my_license_plate_on_photo',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Notification when my license plate on photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='notifications_when_unfamiliar_license_on_photo',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Notification when unfamiliar license plate on photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_license_plate',
            field=models.ManyToManyField(blank=True, null=True, to='profile_and_site_settings.licenseplatelist', verbose_name='User license plate'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_white_list',
            field=models.ManyToManyField(blank=True, null=True, to='profile_and_site_settings.whitelist', verbose_name='User "White list"'),
        ),
    ]
