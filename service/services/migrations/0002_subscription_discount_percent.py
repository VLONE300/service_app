# Generated by Django 3.2.16 on 2024-05-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='discount_percent',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
