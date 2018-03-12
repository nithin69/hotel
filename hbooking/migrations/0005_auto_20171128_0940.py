# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hbooking', '0004_auto_20171123_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='rate',
        ),
        migrations.AddField(
            model_name='rate',
            name='room_type',
            field=models.ForeignKey(blank=True, to='hbooking.Room', null=True),
        ),
    ]
