# Generated by Django 4.2.7 on 2024-01-17 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0004_rename_leetcodetag_leetcodetopic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leetcode',
            old_name='tags',
            new_name='topics',
        ),
    ]
