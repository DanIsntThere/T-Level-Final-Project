# Generated by Django 4.2.11 on 2024-04-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RZA', '0007_alter_profile_loyaltypoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]