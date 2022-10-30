# Generated by Django 3.0 on 2022-10-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imex_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='agent_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'created'), (2, 'pending'), (3, 'verified')], default=1),
        ),
    ]