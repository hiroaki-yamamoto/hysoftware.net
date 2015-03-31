# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_pendingverification_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendingverification',
            name='token_hash',
            field=models.CharField(serialize=False, primary_key=True, default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pendingverification',
            name='email_hash',
            field=models.CharField(unique=True, max_length=40),
            preserve_default=True,
        ),
    ]
