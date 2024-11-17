# Generated by Django 5.1.3 on 2024-11-17 10:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_desktop_networks_wireless_conections_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImacDekstop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('model_title', models.CharField(default='blank', max_length=200)),
                ('brand_name', models.CharField(default='blank', max_length=200)),
                ('processore', models.CharField(default='blank', max_length=400)),
                ('monitor', models.CharField(default='N/A', max_length=200)),
                ('motherboard', models.CharField(default='blank', max_length=400)),
                ('keyboard', models.CharField(default='N/A', max_length=200)),
                ('ram', models.CharField(default='blank', max_length=400)),
                ('graphics_card', models.CharField(blank=True, max_length=400, null=True)),
                ('storage', models.CharField(default='blank', max_length=400)),
                ('networks_wireless_conections', models.CharField(blank=True, max_length=400, null=True)),
                ('operating_system', models.CharField(default='N/A', max_length=100)),
                ('power_supply', models.CharField(blank=True, max_length=400, null=True)),
                ('cpu_cooler', models.CharField(blank=True, max_length=400, null=True)),
                ('casing', models.CharField(default='blank', max_length=400)),
                ('color', models.CharField(default='N/A', max_length=100)),
                ('description', models.TextField(max_length=400)),
                ('status', models.BooleanField(default=False)),
                ('regular_price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('discount_price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('warranty', models.CharField(blank=True, max_length=1, null=True)),
                ('product_code', models.CharField(blank=True, max_length=200, null=True)),
                ('product_release', models.DateTimeField(auto_now_add=True)),
                ('product_catagory', models.CharField(choices=[('DEKSTOP', 'DEKSTOP'), ('GAMINGDEKSTOP', 'GAMINGDEKSTOP'), ('IMAC', 'IMAC')], default='N/A', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='desktop',
            name='keyboard',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AddField(
            model_name='desktop',
            name='monitor',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AddField(
            model_name='desktop',
            name='mouse',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AddField(
            model_name='desktop',
            name='product_catagory',
            field=models.CharField(choices=[('DEKSTOP', 'DEKSTOP'), ('GAMINGDEKSTOP', 'GAMINGDEKSTOP'), ('IMAC', 'IMAC')], default='N/A', max_length=200),
        ),
        migrations.AddField(
            model_name='gamingdesktop',
            name='keyboard',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AddField(
            model_name='gamingdesktop',
            name='monitor',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AddField(
            model_name='gamingdesktop',
            name='mouse',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AddField(
            model_name='gamingdesktop',
            name='product_catagory',
            field=models.CharField(choices=[('DEKSTOP', 'DEKSTOP'), ('GAMINGDEKSTOP', 'GAMINGDEKSTOP'), ('IMAC', 'IMAC')], default='N/A', max_length=200),
        ),
    ]
