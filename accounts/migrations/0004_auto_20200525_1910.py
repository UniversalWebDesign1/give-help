# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-25 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200520_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='county',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='donor',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='donor',
            name='postcode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='street_address1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='donor',
            name='street_address2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='donor',
            name='town_city',
            field=models.CharField(max_length=20),
        ),
    ]
