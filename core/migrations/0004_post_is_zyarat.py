# Generated by Django 4.2.7 on 2023-11-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_content_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_zyarat',
            field=models.BooleanField(default=True),
        ),
    ]
