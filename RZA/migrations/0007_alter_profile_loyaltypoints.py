# Generated by Django 4.2.11 on 2024-04-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RZA', '0006_profile_loyaltypoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='loyaltyPoints',
            field=models.IntegerField(default=0),
        ),
    ]
