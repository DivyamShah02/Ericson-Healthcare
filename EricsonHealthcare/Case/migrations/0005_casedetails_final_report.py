# Generated by Django 5.1 on 2024-12-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Case', '0004_casedetails_city_casedetails_claim_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='casedetails',
            name='final_report',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
