# Generated by Django 3.1 on 2020-08-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200818_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
