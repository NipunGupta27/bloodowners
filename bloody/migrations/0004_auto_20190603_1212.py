# Generated by Django 2.2.1 on 2019-06-03 06:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bloody', '0003_auto_20190603_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2019, 6, 3, 6, 42, 47, 569151, tzinfo=utc)),
        ),
    ]
