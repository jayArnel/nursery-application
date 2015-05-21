# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('svm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='verbose_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='label',
            name='verbose_name',
            field=models.CharField(max_length=50),
        ),
    ]
