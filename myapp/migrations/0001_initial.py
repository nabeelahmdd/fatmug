# Generated by Django 5.0.4 on 2024-04-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('vendor_code', models.CharField(blank=True, max_length=100, unique=True)),
                ('on_time_delivery_rate', models.FloatField(default=0.0)),
                ('quality_rating_avg', models.FloatField(default=0.0)),
                ('average_response_time', models.FloatField(default=0.0)),
                ('fulfillment_rate', models.FloatField(default=0.0)),
            ],
        ),
    ]
