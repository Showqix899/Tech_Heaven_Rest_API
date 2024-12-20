# Generated by Django 5.1.3 on 2024-11-16 18:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('model_title', models.CharField(default='blank', max_length=200)),
                ('brand_name', models.CharField(default='blank', max_length=200)),
                ('processore', models.CharField(default='blank', max_length=400)),
                ('motherboard', models.CharField(default='blank', max_length=400)),
                ('ram', models.CharField(default='blank', max_length=400)),
                ('storage', models.CharField(default='blank', max_length=400)),
                ('power_supply', models.CharField(blank=True, max_length=400, null=True)),
                ('cpu_cooler', models.CharField(blank=True, max_length=400, null=True)),
                ('casing', models.CharField(default='blank', max_length=400)),
                ('description', models.TextField(max_length=400)),
                ('status', models.BooleanField(default=False)),
                ('regular_price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('discount_price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('product_code', models.CharField(blank=True, max_length=200, null=True)),
                ('product_release', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GamingDesktop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('model_title', models.CharField(default='blank', max_length=200)),
                ('brand_name', models.CharField(default='blank', max_length=200)),
                ('processore', models.CharField(default='blank', max_length=400)),
                ('motherboard', models.CharField(default='blank', max_length=400)),
                ('ram', models.CharField(default='blank', max_length=400)),
                ('graphics_card', models.CharField(blank=True, max_length=400, null=True)),
                ('storage', models.CharField(default='blank', max_length=400)),
                ('power_supply', models.CharField(blank=True, max_length=400, null=True)),
                ('cpu_cooler', models.CharField(blank=True, max_length=400, null=True)),
                ('casing', models.CharField(default='blank', max_length=400)),
                ('description', models.TextField(max_length=400)),
                ('status', models.BooleanField(default=False)),
                ('regular_price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('discount_price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('product_code', models.CharField(blank=True, max_length=200, null=True)),
                ('product_release', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
