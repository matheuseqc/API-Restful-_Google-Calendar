# Generated by Django 5.1.1 on 2024-09-08 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('google_event_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
