# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-29 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_auto_20160729_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostlog',
            name='notes',
            field=models.TextField(blank=True, max_length=254, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8'),
        ),
    ]
