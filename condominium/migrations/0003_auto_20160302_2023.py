# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 23:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominium', '0002_customer_dta_nasc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dta_nasc',
            field=models.DateField(default=datetime.datetime(2016, 3, 2, 20, 23, 52, 371663)),
        ),
    ]