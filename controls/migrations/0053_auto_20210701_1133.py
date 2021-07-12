# Generated by Django 3.2.4 on 2021-07-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0052_auto_20210629_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstatement',
            name='statement_type',
            field=models.CharField(blank=True, choices=[('CONTROL_IMPLEMENTATION', 'control_implementation'), ('CONTROL_IMPLEMENTATION_LEGACY', 'control_implementation_legacy'), ('CONTROL_IMPLEMENTATION_PROTOTYPE', 'control_implementation_prototype'), ('ASSESSMENT_RESULT', 'assessment_result'), ('POAM', 'POAM'), ('FISMA_IMPACT_LEVEL', 'fisma_impact_level'), ('SECURITY_IMPACT_LEVEL', 'security_impact_level')], help_text='Statement type.', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='statement_type',
            field=models.CharField(blank=True, choices=[('CONTROL_IMPLEMENTATION', 'control_implementation'), ('CONTROL_IMPLEMENTATION_LEGACY', 'control_implementation_legacy'), ('CONTROL_IMPLEMENTATION_PROTOTYPE', 'control_implementation_prototype'), ('ASSESSMENT_RESULT', 'assessment_result'), ('POAM', 'POAM'), ('FISMA_IMPACT_LEVEL', 'fisma_impact_level'), ('SECURITY_IMPACT_LEVEL', 'security_impact_level')], help_text='Statement type.', max_length=150, null=True),
        ),
    ]