# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160213_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 2, 13, 17, 21, 5, 357262, tzinfo=utc)),
        ),
    ]
