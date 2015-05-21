# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('verbose_name', models.TextField()),
                ('description', models.TextField()),
                ('is_feature', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('verbose_name', models.TextField()),
                ('description', models.TextField()),
                ('code', models.PositiveIntegerField()),
                ('attribute', models.ForeignKey(related_name='labels', to='svm.Attribute')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='dataset',
            field=models.ForeignKey(related_name='attributes', to='svm.Dataset'),
        ),
    ]
