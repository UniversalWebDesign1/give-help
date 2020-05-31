# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-30 13:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200527_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=40)),
                ('total', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(10)])),
            ],
        ),
    ]