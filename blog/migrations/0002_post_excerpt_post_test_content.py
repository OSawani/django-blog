# Generated by Django 4.2.13 on 2024-05-12 14:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='test_content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
