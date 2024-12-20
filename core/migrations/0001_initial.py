# Generated by Django 5.1.4 on 2024-12-20 21:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_time', models.FloatField(default=0.0, help_text='Total audio processing time in seconds.')),
                ('limit', models.FloatField(default=3600.0, help_text='Maximum allowed audio processing time in seconds (default: 1 hour).')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quota', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
