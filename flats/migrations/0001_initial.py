# Generated by Django 5.0.3 on 2024-10-23 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_title', models.CharField(max_length=270)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District Of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=99)),
                ('city', models.CharField(max_length=99)),
                ('type', models.CharField(max_length=99)),
                ('rent_sale', models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale')], max_length=99)),
                ('bedrooms', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], verbose_name='bedrooms')),
                ('condition', models.CharField(max_length=99)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=150)),
                ('flat_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('flat_photo1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('flat_photo2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('flat_photo3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('flat_photo4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_featured', models.BooleanField(max_length=99)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
