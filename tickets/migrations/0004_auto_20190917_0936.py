# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-17 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20190917_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Closed', 'Closed')], max_length=11),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Feature', 'Feature')], max_length=7),
        ),
        migrations.DeleteModel(
            name='TicketStatus',
        ),
        migrations.DeleteModel(
            name='TicketType',
        ),
    ]