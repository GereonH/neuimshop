# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-09 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsfeed',
            old_name='added',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='newsfeed',
            old_name='brand',
            new_name='l1_category',
        ),
        migrations.RenameField(
            model_name='newsfeed',
            old_name='l1_cat',
            new_name='l2_category',
        ),
        migrations.RenameField(
            model_name='newsfeed',
            old_name='l2_cat',
            new_name='l3_category',
        ),
        migrations.RenameField(
            model_name='newsfeed',
            old_name='l3_cat',
            new_name='product_Brand_Name',
        ),
        migrations.RenameField(
            model_name='newsfeed',
            old_name='name',
            new_name='product_Name_de',
        ),
    ]
