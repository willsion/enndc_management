# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-29 16:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20160729_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostlog',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name=b'\xe4\xb8\x8a\xe6\xac\xa1\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='hostlog',
            name='born_time',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
