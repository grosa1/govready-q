# Generated by Django 3.2.13 on 2022-04-29 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0061_proposal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='system',
        ),
    ]