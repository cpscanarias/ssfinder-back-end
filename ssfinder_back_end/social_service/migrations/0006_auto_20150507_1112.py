# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_service', '0005_auto_20150507_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialservice',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
