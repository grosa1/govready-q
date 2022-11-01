# Generated by Django 3.2.16 on 2022-10-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0082_documentid_link_prop_systemtask_timing'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='links',
            field=models.ManyToManyField(blank=True, related_name='element', to='controls.Link'),
        ),
        migrations.AddField(
            model_name='element',
            name='props',
            field=models.ManyToManyField(blank=True, related_name='element', to='controls.Prop'),
        ),
    ]
