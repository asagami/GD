# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GOOD',
            fields=[
                ('GoodID', models.IntegerField(primary_key=True, serialize=False)),
                ('GoodName', models.CharField(default='  ', max_length=20)),
                ('GoodPrice', models.IntegerField()),
                ('GoodPrice1', models.IntegerField()),
                ('GoodPrice2', models.IntegerField()),
                ('GoodImage', models.ImageField(upload_to='')),
            ],
        ),
    ]
