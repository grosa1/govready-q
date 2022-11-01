# Generated by Django 3.2.16 on 2022-10-31 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0088_element_lastmodified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='documents',
            field=models.ManyToManyField(blank=True, help_text='A document identifier qualified by an identifier scheme.', related_name='documents', to='controls.DocumentId'),
        ),
        migrations.AlterField(
            model_name='element',
            name='revisions',
            field=models.ManyToManyField(blank=True, help_text='An entry in a sequential list of revisions to the containing document in reverse chronological order (i.e., most recent previous revision first).', related_name='revisions', to='controls.Revision'),
        ),
    ]
