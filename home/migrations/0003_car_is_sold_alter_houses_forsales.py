# Generated by Django 5.0.4 on 2024-08-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_houses_rename_cars_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='houses',
            name='forsales',
            field=models.BooleanField(default=False),
        ),
    ]
