# Generated by Django 5.0.6 on 2024-07-01 01:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_record_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]