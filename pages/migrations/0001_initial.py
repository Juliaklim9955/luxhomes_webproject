# Generated by Django 5.0.3 on 2024-10-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('fb_link', models.URLField(max_length=250)),
                ('x_link', models.URLField(max_length=250)),
                ('google_link', models.URLField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
