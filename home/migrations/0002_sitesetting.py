# Generated by Django 5.1.6 on 2025-02-27 17:24

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', colorfield.fields.ColorField(default='#000000', image_field=None, max_length=25, samples=None)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/')),
            ],
        ),
    ]
