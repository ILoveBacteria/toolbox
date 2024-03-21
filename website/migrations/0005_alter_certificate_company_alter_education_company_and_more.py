# Generated by Django 4.2.5 on 2023-09-06 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_company_remove_certificate_company_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='website.company'),
        ),
        migrations.AlterField(
            model_name='education',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='website.company'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='website.company'),
        ),
    ]