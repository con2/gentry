# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=64)),
                ('type', models.CharField(default='unknown', max_length=32)),
                ('message', models.CharField(blank=True, max_length=128)),
                ('culprit', models.CharField(blank=True, max_length=128)),
                ('level', models.CharField(blank=True, max_length=32)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('timestamp', models.DateTimeField(db_index=True, editable=False)),
                ('data', models.TextField(blank=True, editable=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gore.Project')),
            ],
        ),
    ]
