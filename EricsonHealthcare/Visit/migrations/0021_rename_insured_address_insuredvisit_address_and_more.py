# Generated by Django 5.1 on 2025-02-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visit', '0020_alter_visit_type_of_visit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insuredvisit',
            old_name='insured_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='insuredvisit',
            old_name='insured_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='insuredvisit',
            old_name='insured_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='insuredvisit',
            old_name='insured_contact_number',
            new_name='contact_number',
        ),
        migrations.RenameField(
            model_name='insuredvisit',
            old_name='insured_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='insuredvisit',
            old_name='insured_state',
            new_name='state',
        ),
        migrations.AlterField(
            model_name='visit',
            name='type_of_visit',
            field=models.CharField(choices=[('Hospital', 'Hospital'), ('Treating_doctor', 'Treating Doctor'), ('Lab', 'Lab'), ('Chemist', 'Chemist'), ('Insured', 'Insured')], max_length=50),
        ),
    ]
