# Generated by Django 4.1.7 on 2023-06-18 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MonaAppForm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitorrequest',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='monitorrequest',
            name='expire_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]