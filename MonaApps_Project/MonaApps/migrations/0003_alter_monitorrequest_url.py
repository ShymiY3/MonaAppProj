# Generated by Django 4.1.7 on 2023-04-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonaApps', '0002_monitorrequest_interval_monitorrequest_notification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitorrequest',
            name='URL',
            field=models.CharField(max_length=200),
        ),
    ]