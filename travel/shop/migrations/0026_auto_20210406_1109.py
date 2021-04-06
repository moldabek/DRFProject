# Generated by Django 2.2.6 on 2021-04-06 05:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20210222_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('abaa96d2-25b8-4e61-aa29-d3e13a6a6587'), unique=True, verbose_name='Номер билета'),
        ),
    ]