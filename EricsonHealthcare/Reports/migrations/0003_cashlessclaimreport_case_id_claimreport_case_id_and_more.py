# Generated by Django 5.1 on 2024-12-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0002_cashlessclaimreport_claimreport_hdcclosurereport_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashlessclaimreport',
            name='case_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='claimreport',
            name='case_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hdcclosurereport',
            name='case_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='healthclaimreport',
            name='case_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iclmclosurereport',
            name='case_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='padeathreport',
            name='case_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='securemindcriticalillnessreport',
            name='case_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ttdreport',
            name='case_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
