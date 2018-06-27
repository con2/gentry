# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-25 15:32
from __future__ import unicode_literals

from django.db import migrations, transaction


def group_all_events(apps, schema_editor):
    # Using apps.get_model() won't work here anyway,
    # so we can use the utility in gore.utils.event_groups
    import gore.utils.event_grouper as eg
    with transaction.atomic():
        eg.group_all_events()


class Migration(migrations.Migration):
    dependencies = [
        ('gore', '0004_event_group'),
    ]

    operations = [
        migrations.RunPython(
            group_all_events,
            migrations.RunPython.noop,
        )
    ]
