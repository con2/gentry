# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('key', models.CharField(db_index=True, editable=True, max_length=64)),
                ('secret', models.CharField(db_index=True, editable=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=128)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='key',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gore.Project'),
        ),
    ]
