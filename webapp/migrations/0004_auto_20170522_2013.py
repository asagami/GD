# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 20:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20170522_2012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enterprise_order',
            old_name='UserName',
            new_name='UserID',
        ),
    ]
