# Generated by Django 3.1 on 2020-08-18 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200818_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/blog'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]