# Generated by Django 3.2.4 on 2023-11-30 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Workouts', '0002_auto_20231120_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='C_time',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
