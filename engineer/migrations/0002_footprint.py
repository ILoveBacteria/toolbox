# Generated by Django 4.2.6 on 2023-11-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField()),
                ('tags', models.ManyToManyField(to='engineer.tag')),
            ],
        ),
    ]
