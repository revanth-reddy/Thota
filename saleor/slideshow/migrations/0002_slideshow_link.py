# Generated by Django 2.2.9 on 2020-08-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slideshow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
