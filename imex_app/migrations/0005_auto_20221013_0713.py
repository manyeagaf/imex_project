# Generated by Django 3.0 on 2022-10-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imex_app', '0004_auto_20221013_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_active',
        ),
        migrations.AddField(
            model_name='profile',
            name='license',
            field=models.ImageField(blank=True, null=True, upload_to='license'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
