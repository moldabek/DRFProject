# Generated by Django 2.2.6 on 2019-11-10 09:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20191110_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('c3c7c01e-1af1-45d4-bbc5-d58559622ac6'), unique=True, verbose_name='Номер билета'),
        ),
    ]