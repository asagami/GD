# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 04:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0004_auto_20170522_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='useradd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserTelephone', models.IntegerField()),
                ('UserAddress_deafult', models.CharField(max_length=100)),
                ('UserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='enterprise_order',
            old_name='GooDID',
            new_name='GoodID',
        ),
        migrations.AddField(
            model_name='good',
            name='GoodStock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='enterprise_order',
            name='ADDRESS',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='enterprise_order',
            name='Status',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='pay',
            name='OrderID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.enterprise_ORDER'),
        ),
        migrations.AddField(
            model_name='pay',
            name='Username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
