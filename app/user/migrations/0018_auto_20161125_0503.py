# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20161124_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingLanguage',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('icon_cls', models.CharField(blank=True, max_length=20, null=True)),
                ('icon_body', models.CharField(blank=True, max_length=20, null=True)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('languages', models.ManyToManyField(related_name='frameworks', to='user.CodingLanguage')),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='availability',
            field=models.CharField(choices=[('FL', 'Available for Full-Time and Part-Time position'), ('PT', 'Available for Part-Time position only'), ('NA', 'Busy')], db_index=True, max_length=2),
        ),
        migrations.AddField(
            model_name='codinglanguage',
            name='users_info',
            field=models.ManyToManyField(related_name='coding_languages', to='user.UserInfo'),
        ),
    ]