# Generated by Django 5.0.3 on 2024-10-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0006_alter_flat_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
