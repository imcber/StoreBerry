# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 16:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perfil',
            new_name='UserComprador',
        ),
    ]
