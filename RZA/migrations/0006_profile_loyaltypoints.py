# Generated by Django 4.2.11 on 2024-04-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RZA', '0005_booking_user_hotel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='loyaltyPoints',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
