# Generated by Django 4.0 on 2022-04-01 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingapp', '0003_rename_create_team_team_count_create_team_create_team_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='acntspayslip',
            name='acntspayslip_esitype',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='acntspayslip',
            name='acntspayslip_pftype',
            field=models.CharField(default='', max_length=255),
        ),
    ]
