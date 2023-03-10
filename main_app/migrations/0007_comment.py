# Generated by Django 4.1.7 on 2023-03-08 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_project_members_alter_project_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(max_length=250)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.project')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
