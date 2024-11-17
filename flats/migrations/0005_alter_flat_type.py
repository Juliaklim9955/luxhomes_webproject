# Generated by Django 5.0.3 on 2024-10-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0004_alter_flat_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='type',
            field=models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Penthouse', 'Penthouse'), ('Entire Building', 'Entrie Building')], max_length=99),
        ),
    ]