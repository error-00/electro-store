# Generated by Django 5.0.6 on 2024-06-10 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.rating'),
        ),
    ]
