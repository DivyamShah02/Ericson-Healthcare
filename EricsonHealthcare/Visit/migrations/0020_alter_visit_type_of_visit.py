# Generated by Django 5.1 on 2025-02-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visit', '0019_insuredvisit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='type_of_visit',
            field=models.CharField(choices=[('Hospital', 'Hospital'), ('Treating_doctor', 'Treating Doctor'), ('Lab', 'Lab'), ('Chemist', 'Chemist'), ('Insured Visit', 'Insured Visit')], max_length=50),
        ),
    ]
