# Generated by Django 4.1.7 on 2024-01-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='total_cost',
            field=models.IntegerField(default=0),
        ),
    ]
