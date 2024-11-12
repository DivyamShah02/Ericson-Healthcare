# Generated by Django 5.1.3 on 2024-11-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Case', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='data_entry_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='medical_officer_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='casedetails',
            name='claim_approved_amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='casedetails',
            name='medical_officer_remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casedetails',
            name='status_of_claim',
            field=models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Reject', 'Reject')], max_length=50, null=True),
        ),
    ]
