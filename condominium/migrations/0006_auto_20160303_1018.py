# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominium', '0005_auto_20160303_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='customer',
            name='cep',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='customer',
            name='compl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='number',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
    ]
