# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EthBtc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('bid', models.FloatField()),
                ('ask', models.FloatField()),
                ('eth_balance', models.FloatField()),
                ('btc_balance', models.FloatField()),
            ],
        ),
    ]
