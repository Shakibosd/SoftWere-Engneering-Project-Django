# Generated by Django 5.0.6 on 2024-06-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musician', '0002_remove_musician_instrument_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='instrument_type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]