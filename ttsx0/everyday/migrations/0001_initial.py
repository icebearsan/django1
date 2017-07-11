# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('umail', models.CharField(max_length=30)),
                ('urec', models.CharField(max_length=20, default='')),
                ('uaddress', models.CharField(max_length=30, default='')),
                ('ucode', models.CharField(max_length=6, default='')),
                ('uphone', models.CharField(max_length=11, default='')),
            ],
        ),
    ]
