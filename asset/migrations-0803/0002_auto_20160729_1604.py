# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-29 16:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostlog',
            name='peo',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request', to=settings.AUTH_USER_MODEL),
        ),
    ]
