# Generated by Django 4.2.5 on 2023-09-06 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_certificate_company_image_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='company_image_url',
        ),
        migrations.RemoveField(
            model_name='education',
            name='company_image_url',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='company_image_url',
        ),
        migrations.AddField(
            model_name='certificate',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='website.company'),
        ),
        migrations.AddField(
            model_name='education',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='website.company'),
        ),
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='website.company'),
        ),
    ]
