# Generated by Django 4.0 on 2021-12-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
