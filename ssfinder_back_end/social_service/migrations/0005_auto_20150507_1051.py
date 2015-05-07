# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_service', '0004_auto_20150505_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=80)),
                ('postal_code', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=40)),
                ('description', models.TextField(help_text=b'Optional', max_length=400, verbose_name=b'Description', blank=True)),
                ('web', models.CharField(max_length=50, blank=True)),
                ('facebook', models.CharField(max_length=50, blank=True)),
                ('twitter', models.CharField(max_length=30, blank=True)),
                ('instagram', models.CharField(max_length=50, blank=True)),
                ('google_plus', models.CharField(max_length=50, blank=True)),
                ('tumblr', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'Social Service',
                'verbose_name_plural': 'Social Services',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='socialservice',
            name='categories',
            field=models.ManyToManyField(to='social_service.Category'),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='town',
            field=models.ForeignKey(to='social_service.Town'),
        ),
    ]
