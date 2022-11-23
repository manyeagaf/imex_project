# Generated by Django 4.1.3 on 2022-11-23 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=205, null=True)),
                ('type', models.CharField(max_length=200)),
                ('type_image', models.ImageField(blank=True, null=True, upload_to='type_images')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField(blank=True, max_length=250, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('telephone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(blank=True, default='/profile/profile1.jpeg', null=True, upload_to='profile')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'client'), (2, 'agent')], default=1)),
                ('license', models.ImageField(blank=True, null=True, upload_to='license')),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('company_description', models.TextField(blank=True, null=True)),
                ('company_location', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('region', models.CharField(blank=True, max_length=200, null=True)),
                ('is_sea_port', models.BooleanField(default=False)),
                ('ghana_card', models.CharField(max_length=100)),
                ('is_air_port', models.BooleanField(default=False)),
                ('agent_status', models.PositiveSmallIntegerField(choices=[(1, 'created'), (2, 'pending'), (3, 'verified')], default=1)),
                ('agent_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='imex_app.agenttype')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('code_active', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
