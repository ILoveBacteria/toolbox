# Generated by Django 4.2.10 on 2024-07-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0006_vocabulary'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='translation',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]