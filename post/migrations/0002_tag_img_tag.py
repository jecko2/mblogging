# Generated by Django 4.1.3 on 2022-11-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='img_tag',
            field=models.ImageField(blank=True, null=True, upload_to='tags/'),
        ),
    ]
