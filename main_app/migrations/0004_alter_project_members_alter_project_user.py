# Generated by Django 4.1.7 on 2023-03-07 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_project_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='project_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
