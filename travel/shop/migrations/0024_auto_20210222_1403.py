# Generated by Django 2.2.6 on 2021-02-22 08:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20210222_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('c175b7d6-c16c-48b8-83e8-171d5bfcdec6'), unique=True, verbose_name='Номер билета'),
        ),
    ]
