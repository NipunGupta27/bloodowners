# Generated by Django 2.2.1 on 2019-06-03 06:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bloody', '0002_auto_20190531_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2019, 6, 3, 6, 42, 15, 145372, tzinfo=utc)),
        ),
    ]
