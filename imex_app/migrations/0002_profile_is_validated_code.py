# Generated by Django 4.1.3 on 2022-12-12 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imex_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_validated',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_generated', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiring_date', models.DateTimeField()),
                ('unique_code', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]