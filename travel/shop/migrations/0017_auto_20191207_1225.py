# Generated by Django 2.2.6 on 2019-12-07 06:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20191206_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('5f7d33fb-8d98-401a-a574-8bdc70a6e869'), unique=True, verbose_name='Номер билета'),
        ),
    ]
