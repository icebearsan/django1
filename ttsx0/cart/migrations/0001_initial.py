# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('everyday', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='goods.GoodsInfo')),
                ('user', models.ForeignKey(to='everyday.UserInfo')),
            ],
        ),
    ]
