# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-10-23 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('describe', models.TextField(verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
    ]
