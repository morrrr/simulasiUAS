# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='text',
            new_name='status',
        ),
        migrations.AddField(
            model_name='item',
            name='angka',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='tebakan',
            field=models.IntegerField(default=0),
        ),
    ]
