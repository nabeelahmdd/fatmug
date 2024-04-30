# Generated by Django 5.0.4 on 2024-04-29 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_purchaseorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.vendor')),
            ],
        ),
    ]
