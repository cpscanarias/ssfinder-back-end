# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_service', '0002_aacc_province_town'),
    ]

    operations = [
        migrations.AddField(
            model_name='province',
            name='aacc',
            field=models.ForeignKey(default=1, to='social_service.AACC'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='town',
            name='province',
            field=models.ForeignKey(default=1, to='social_service.Province'),
            preserve_default=False,
        ),
    ]
