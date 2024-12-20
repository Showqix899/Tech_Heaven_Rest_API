# Generated by Django 5.1.3 on 2024-11-18 13:58

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_imacdekstop_desktop_keyboard_desktop_monitor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamingLaptop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('model_title', models.CharField(default='blank', max_length=200)),
                ('brand_name', models.CharField(default='blank', max_length=200)),
                ('processore', models.CharField(default='blank', max_length=400)),
                ('processore_frequency', models.CharField(default='N/A', max_length=50)),
                ('processore_core', models.CharField(default='N/A', max_length=30)),
                ('processore_thread', models.CharField(default='N/A', max_length=30)),
                ('cpu_cache', models.CharField(default='N/A', max_length=30)),
                ('display', models.CharField(default='N/A', max_length=100)),
                ('refresh_rate', models.CharField(default='N/A', max_length=10)),
                ('ram', models.CharField(max_length=20)),
                ('ram_type', models.CharField(max_length=30)),
                ('ram_slot', models.IntegerField(default=1)),
                ('ram_capacity', models.IntegerField(default=8)),
                ('operating_system', models.CharField(default='N/A', max_length=100)),
                ('storege', models.IntegerField(default=128)),
                ('storege_type', models.CharField(default='M.2', max_length=30)),
                ('storege_slot', models.IntegerField(default=1)),
                ('graphics_card', models.CharField(blank=True, max_length=400, null=True)),
                ('keyboard_type', models.CharField(default='N/A', max_length=30)),
                ('touchpad', models.BooleanField(default=False)),
                ('camera', models.CharField(default='N/A', max_length=30)),
                ('microphone', models.BooleanField(default=False)),
                ('speaker', models.BooleanField(default=False)),
                ('optical_drive', models.CharField(default='N/A', max_length=30)),
                ('card_reader', models.CharField(default='N/A', max_length=30)),
                ('usb_ports', models.CharField(default='N/A', max_length=100)),
                ('headphone_jack', models.BooleanField(default=False)),
                ('network_wifi', models.CharField(default='N/A', max_length=100)),
                ('fringerprint_sensore', models.BooleanField(default=False)),
                ('battery', models.CharField(default='N/A', max_length=100)),
                ('battery_capacity', models.CharField(default='N/A', max_length=100)),
                ('dimension', models.CharField(default='N/A', max_length=100)),
                ('weight', models.CharField(default='N/A', max_length=100)),
                ('body_metarial', models.CharField(default='N/A', max_length=100)),
                ('color', models.CharField(default='N/A', max_length=100)),
                ('description', models.TextField(max_length=400)),
                ('status', models.BooleanField(default=False)),
                ('regular_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('warranty', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('model_title', models.CharField(default='blank', max_length=200)),
                ('brand_name', models.CharField(default='blank', max_length=200)),
                ('processore', models.CharField(default='blank', max_length=400)),
                ('processore_frequency', models.CharField(default='N/A', max_length=50)),
                ('processore_core', models.CharField(default='N/A', max_length=30)),
                ('processore_thread', models.CharField(default='N/A', max_length=30)),
                ('cpu_cache', models.CharField(default='N/A', max_length=30)),
                ('display', models.CharField(default='N/A', max_length=100)),
                ('refresh_rate', models.CharField(default='N/A', max_length=10)),
                ('ram', models.CharField(max_length=20)),
                ('ram_type', models.CharField(max_length=30)),
                ('ram_slot', models.IntegerField(default=1)),
                ('ram_capacity', models.IntegerField(default=8)),
                ('operating_system', models.CharField(default='N/A', max_length=100)),
                ('storege', models.IntegerField(default=128)),
                ('storege_type', models.CharField(default='M.2', max_length=30)),
                ('storege_slot', models.IntegerField(default=1)),
                ('graphix_model', models.CharField(default='N/A', max_length=30)),
                ('graphics_memory', models.CharField(default='shared', max_length=30)),
                ('keyboard_type', models.CharField(default='N/A', max_length=30)),
                ('touchpad', models.BooleanField(default=False)),
                ('camera', models.CharField(default='N/A', max_length=30)),
                ('microphone', models.BooleanField(default=False)),
                ('speaker', models.BooleanField(default=False)),
                ('optical_drive', models.CharField(default='N/A', max_length=30)),
                ('card_reader', models.CharField(default='N/A', max_length=30)),
                ('usb_ports', models.CharField(default='N/A', max_length=100)),
                ('headphone_jack', models.BooleanField(default=False)),
                ('network_wifi', models.CharField(default='N/A', max_length=100)),
                ('fringerprint_sensore', models.BooleanField(default=False)),
                ('battery', models.CharField(default='N/A', max_length=100)),
                ('battery_capacity', models.CharField(default='N/A', max_length=100)),
                ('dimension', models.CharField(default='N/A', max_length=100)),
                ('weight', models.CharField(default='N/A', max_length=100)),
                ('body_metarial', models.CharField(default='N/A', max_length=100)),
                ('color', models.CharField(default='N/A', max_length=100)),
                ('description', models.TextField(max_length=400)),
                ('status', models.BooleanField(default=False)),
                ('regular_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('warranty', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mackbook',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('model_title', models.CharField(default='blank', max_length=200)),
                ('brand_name', models.CharField(default='blank', max_length=200)),
                ('processore', models.CharField(default='blank', max_length=400)),
                ('processore_frequency', models.CharField(default='N/A', max_length=50)),
                ('processore_core', models.CharField(default='N/A', max_length=30)),
                ('processore_thread', models.CharField(default='N/A', max_length=30)),
                ('cpu_cache', models.CharField(default='N/A', max_length=30)),
                ('display', models.CharField(default='N/A', max_length=100)),
                ('refresh_rate', models.CharField(default='N/A', max_length=10)),
                ('ram', models.CharField(max_length=20)),
                ('ram_type', models.CharField(max_length=30)),
                ('ram_slot', models.IntegerField(default=1)),
                ('ram_capacity', models.IntegerField(default=8)),
                ('operating_system', models.CharField(default='N/A', max_length=100)),
                ('storege', models.IntegerField(default=128)),
                ('storege_type', models.CharField(default='M.2', max_length=30)),
                ('storege_slot', models.IntegerField(default=1)),
                ('graphix_model', models.CharField(default='N/A', max_length=30)),
                ('graphics_memory', models.CharField(default='shared', max_length=30)),
                ('keyboard_type', models.CharField(default='N/A', max_length=30)),
                ('touchpad', models.BooleanField(default=False)),
                ('camera', models.CharField(default='N/A', max_length=30)),
                ('microphone', models.BooleanField(default=False)),
                ('speaker', models.BooleanField(default=False)),
                ('optical_drive', models.CharField(default='N/A', max_length=30)),
                ('card_reader', models.CharField(default='N/A', max_length=30)),
                ('usb_ports', models.CharField(default='N/A', max_length=100)),
                ('headphone_jack', models.BooleanField(default=False)),
                ('network_wifi', models.CharField(default='N/A', max_length=100)),
                ('fringerprint_sensore', models.BooleanField(default=False)),
                ('battery', models.CharField(default='N/A', max_length=100)),
                ('battery_capacity', models.CharField(default='N/A', max_length=100)),
                ('dimension', models.CharField(default='N/A', max_length=100)),
                ('weight', models.CharField(default='N/A', max_length=100)),
                ('body_metarial', models.CharField(default='N/A', max_length=100)),
                ('color', models.CharField(default='N/A', max_length=100)),
                ('description', models.TextField(max_length=400)),
                ('status', models.BooleanField(default=False)),
                ('regular_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('warranty', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='desktop',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='regular_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='gamingdesktop',
            name='discount_price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='gamingdesktop',
            name='regular_price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='imacdekstop',
            name='discount_price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='imacdekstop',
            name='regular_price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
