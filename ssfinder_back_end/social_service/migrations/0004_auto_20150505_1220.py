# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_service', '0003_auto_20150504_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='town',
            name='code',
        ),
        migrations.AlterField(
            model_name='aacc',
            name='code',
            field=models.CharField(unique=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='province',
            name='code',
            field=models.CharField(unique=True, max_length=5),
        ),
    ]
