# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20161121_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='GithubProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_url', models.URLField()),
                ('html_url', models.URLField()),
                ('bio', models.CharField(max_length=160)),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='github_user_info',
        ),
        migrations.AddField(
            model_name='githubprofile',
            name='user_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo'),
        ),
    ]
