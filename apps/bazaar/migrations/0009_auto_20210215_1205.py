# Generated by Django 3.1.6 on 2021-02-15 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0008_remove_request_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('1', 'open'), ('2', 'accepted'), ('3', 'deleted')], default=1, max_length=1),
        ),
    ]