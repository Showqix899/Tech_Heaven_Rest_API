# Generated by Django 5.1.3 on 2024-11-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktop',
            name='networks_wireless_conections',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='desktop',
            name='operating_system',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='desktop',
            name='warranty',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='gamingdesktop',
            name='networks_wireless_conections',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='gamingdesktop',
            name='operating_system',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='gamingdesktop',
            name='warranty',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
