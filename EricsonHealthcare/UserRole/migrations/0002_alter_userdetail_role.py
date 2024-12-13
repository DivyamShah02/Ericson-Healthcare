# Generated by Django 5.1 on 2024-12-11 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserRole', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='role',
            field=models.CharField(choices=[('hod', 'HOD'), ('coordinator', 'Coordinator'), ('investigator', 'InvestigatingOfficer'), ('medical_officer', 'MedicalOfficer'), ('data_entry_personnel', 'DataEntryPersonnel'), ('admin', 'Admin')], max_length=20),
        ),
    ]