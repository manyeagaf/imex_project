# Generated by Django 3.0 on 2022-10-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imex_app', '0008_auto_20221005_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
    ]
