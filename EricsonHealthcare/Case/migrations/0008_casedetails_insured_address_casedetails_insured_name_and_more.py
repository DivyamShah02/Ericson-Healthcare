# Generated by Django 5.1 on 2025-01-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Case', '0007_remove_insurancecompany_gc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='casedetails',
            name='insured_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='casedetails',
            name='insured_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casedetails',
            name='insured_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
