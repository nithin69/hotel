# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hbooking', '0003_auto_20171123_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='arrival_date',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='departure_date',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
