# Generated by Django 5.1 on 2024-12-25 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visit', '0003_alter_hospitalvisit_doa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalvisit',
            name='answers',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='labvisit',
            name='answers',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pharmacyvisit',
            name='answers',
            field=models.JSONField(blank=True, null=True),
        ),
    ]