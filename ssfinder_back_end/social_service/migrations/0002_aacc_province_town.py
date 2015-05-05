# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AACC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Autonomous Community',
                'verbose_name_plural': 'Autonomous Comunities',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Province',
                'verbose_name_plural': 'Provinces',
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Town',
                'verbose_name_plural': 'Towns',
            },
        ),
    ]
