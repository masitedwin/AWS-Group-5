# Generated by Django 5.1.6 on 2025-03-25 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('manager', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyClubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=300)),
                ('zip_code', models.CharField(max_length=12, verbose_name='Zip/Post Code')),
                ('phone', models.CharField(max_length=20, verbose_name='Contact Phone')),
                ('web', models.URLField(verbose_name='Website Address')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(verbose_name='Booking Date')),
                ('guest_num', models.PositiveSmallIntegerField(verbose_name='Number of Guests')),
                ('notes', models.TextField(blank=True, verbose_name='Booking Notes')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.event')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.myclubuser')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, through='Events.Booking', to='Events.myclubuser'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Events.venue'),
        ),
    ]
