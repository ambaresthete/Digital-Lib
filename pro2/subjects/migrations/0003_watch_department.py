# Generated by Django 2.0.5 on 2018-07-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_watch_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='department',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
