# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hbooking', '0002_location_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='arrival_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='departure_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
