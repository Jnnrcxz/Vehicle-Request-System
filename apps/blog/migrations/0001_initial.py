# Generated by Django 3.2 on 2023-01-05 07:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('shortdescription', models.CharField(blank=True, max_length=250, null=True)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='blog/header_images/')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
