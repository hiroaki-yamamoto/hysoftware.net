# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NotaionTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('act', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legal.Act')),
            ],
        ),
        migrations.CreateModel(
            name='RecognizedCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Recognized Countries',
            },
        ),
        migrations.AddField(
            model_name='act',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legal.RecognizedCountry'),
        ),
    ]