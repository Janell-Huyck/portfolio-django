# Generated by Django 3.0.6 on 2020-07-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('language', models.CharField(blank=True, choices=[('JS', 'JavaScript'), ('DJ', 'Django'), ('RR', 'React-Redux'), ('RE', 'React'), ('PY', 'Python')], max_length=2, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('site_url', models.URLField(blank=True, null=True)),
                ('repository', models.URLField(blank=True, null=True)),
                ('picture_1', models.FilePathField(blank=True, null=True, path='static/img', recursive=True)),
                ('picture_2', models.FilePathField(blank=True, null=True, path='static/img', recursive=True)),
                ('picture_3', models.FilePathField(blank=True, null=True, path='static/img', recursive=True)),
                ('picture_4', models.FilePathField(blank=True, null=True, path='static/img', recursive=True)),
                ('is_featured', models.BooleanField(blank=True, default=False, null=True)),
                ('display_order', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
