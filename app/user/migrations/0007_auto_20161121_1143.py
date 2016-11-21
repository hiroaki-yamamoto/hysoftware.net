# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20161121_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubprofile',
            name='user_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='github_profile', to='user.UserInfo'),
        ),
    ]
