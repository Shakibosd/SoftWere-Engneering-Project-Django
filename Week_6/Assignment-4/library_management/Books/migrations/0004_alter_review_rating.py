# Generated by Django 5.0.6 on 2024-06-29 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_alter_review_rating_customuser_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '1 - Poor'), ('2', '2 - Fair'), ('3', '3 - Good'), ('4', '4 - Very Good'), ('5', '5 - Excellent')], max_length=10, null=True),
        ),
    ]
