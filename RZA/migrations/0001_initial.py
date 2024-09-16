# Generated by Django 4.2.11 on 2024-04-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('num_adult_tickets', models.IntegerField(default=0)),
                ('num_child_tickets', models.IntegerField(default=0)),
                ('num_senior_tickets', models.IntegerField(default=0)),
            ],
        ),
    ]