# Generated by Django 3.2.7 on 2021-09-12 05:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 5, 55, 15, 678111, tzinfo=utc), verbose_name='closed date'),
            preserve_default=False,
        ),
    ]
