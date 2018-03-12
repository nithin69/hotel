# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, null=True, blank=True)),
                ('description_para1', models.TextField(null=True, blank=True)),
                ('description_para2', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'about', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arrival_date', models.CharField(max_length=40, null=True, blank=True)),
                ('departure_date', models.CharField(max_length=40, null=True, blank=True)),
                ('adults', models.IntegerField(null=True, blank=True)),
                ('children', models.IntegerField(null=True, blank=True)),
                ('no_of_rooms', models.IntegerField(null=True, blank=True)),
                ('no_of_days', models.IntegerField(null=True, blank=True)),
                ('status', models.CharField(blank=True, max_length=40, null=True, choices=[(b'Available', b'Available'), (b'Not Available', b'Not Available')])),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=10, null=True, blank=True)),
                ('txnid', models.CharField(max_length=40, null=True, blank=True)),
                ('amount', models.CharField(max_length=40, null=True, blank=True)),
                ('firstname', models.CharField(max_length=40, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('phone', models.CharField(max_length=40, null=True, blank=True)),
                ('productinfo', models.TextField(null=True, blank=True)),
                ('surl', models.CharField(max_length=255, null=True, blank=True)),
                ('furl', models.CharField(max_length=255, null=True, blank=True)),
                ('hash_key', models.CharField(max_length=255, null=True, blank=True)),
                ('udf1', models.CharField(max_length=25, null=True, verbose_name=b'City', blank=True)),
                ('udf2', models.CharField(max_length=25, null=True, verbose_name=b'Address', blank=True)),
                ('udf3', models.CharField(max_length=25, null=True, verbose_name=b'State', blank=True)),
                ('udf4', models.CharField(max_length=25, null=True, verbose_name=b'Country', blank=True)),
                ('udf5', models.CharField(max_length=25, null=True, verbose_name=b'Pincode', blank=True)),
                ('arrival_date', models.CharField(max_length=25, null=True, blank=True)),
                ('departure_date', models.CharField(max_length=25, null=True, blank=True)),
                ('no_of_rooms', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Booking',
            },
        ),
        migrations.CreateModel(
            name='Bulk_rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateField(null=True, blank=True)),
                ('to_date', models.DateField(null=True, blank=True)),
                ('rate', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('subject', models.CharField(max_length=40, null=True, blank=True)),
                ('message', models.TextField(null=True, blank=True)),
                ('phone', models.CharField(max_length=40, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'facility', blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'gallery', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.CharField(max_length=255, null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('image1', models.ImageField(null=True, upload_to=b'rooms', blank=True)),
                ('image2', models.ImageField(null=True, upload_to=b'rooms', blank=True)),
                ('image3', models.ImageField(null=True, upload_to=b'rooms', blank=True)),
                ('image4', models.ImageField(null=True, upload_to=b'rooms', blank=True)),
                ('image5', models.ImageField(null=True, upload_to=b'rooms', blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('occupancy', models.CharField(max_length=50, null=True, blank=True)),
                ('size', models.CharField(max_length=50, null=True, blank=True)),
                ('view', models.CharField(max_length=255, null=True, blank=True)),
                ('room_service', models.CharField(max_length=255, null=True, blank=True)),
                ('terraces', models.CharField(max_length=255, null=True, blank=True)),
                ('free_pickup_facilty', models.BooleanField(default=True)),
                ('internet_free', models.BooleanField(default=True)),
                ('gym', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('available_rooms', models.IntegerField(null=True, blank=True)),
                ('arrival_date', models.CharField(max_length=40, null=True, blank=True)),
                ('departure_date', models.CharField(max_length=40, null=True, blank=True)),
                ('adults', models.IntegerField(null=True, blank=True)),
                ('children', models.IntegerField(null=True, blank=True)),
                ('no_of_rooms', models.IntegerField(null=True, blank=True)),
                ('no_of_days', models.IntegerField(null=True, blank=True)),
                ('status', models.CharField(blank=True, max_length=40, null=True, choices=[(b'Available', b'Available'), (b'Not Available', b'Not Available')])),
                ('location', models.ForeignKey(blank=True, to='hbooking.Location', null=True)),
                ('rate', models.ManyToManyField(to='hbooking.Rate', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spiritual_tours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('description_para1', models.TextField(null=True, blank=True)),
                ('description_para2', models.TextField(null=True, blank=True)),
                ('description_para3', models.TextField(null=True, blank=True)),
                ('image1', models.ImageField(null=True, upload_to=b'spiritual', blank=True)),
                ('image2', models.ImageField(null=True, upload_to=b'spiritual', blank=True)),
                ('image3', models.ImageField(null=True, upload_to=b'spiritual', blank=True)),
                ('image4', models.ImageField(null=True, upload_to=b'spiritual', blank=True)),
                ('image5', models.ImageField(null=True, upload_to=b'spiritual', blank=True)),
                ('image6', models.ImageField(null=True, upload_to=b'spiritual', blank=True)),
                ('location', models.ForeignKey(blank=True, to='hbooking.Location', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='location',
            field=models.ForeignKey(blank=True, to='hbooking.Location', null=True),
        ),
        migrations.AddField(
            model_name='facility',
            name='location',
            field=models.ForeignKey(blank=True, to='hbooking.Location', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.ForeignKey(blank=True, to='hbooking.Location', null=True),
        ),
        migrations.AddField(
            model_name='bulk_rate',
            name='room_type',
            field=models.ForeignKey(blank=True, to='hbooking.Room', null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='room_type',
            field=models.ForeignKey(blank=True, to='hbooking.Room', null=True),
        ),
        migrations.AddField(
            model_name='availability',
            name='room',
            field=models.ForeignKey(to='hbooking.Room'),
        ),
        migrations.AddField(
            model_name='about',
            name='location',
            field=models.ForeignKey(blank=True, to='hbooking.Location', null=True),
        ),
    ]
