# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-09 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=300)),
                ('l1_cat', models.CharField(max_length=300)),
                ('l2_cat', models.CharField(max_length=300)),
                ('l3_cat', models.CharField(max_length=300)),
                ('brand', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('url', models.CharField(max_length=300)),
                ('added', models.CharField(max_length=300)),
            ],
        ),
    ]