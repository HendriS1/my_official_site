# Generated by Django 4.1.6 on 2023-03-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('event_date', models.DateTimeField()),
                ('venue', models.CharField(max_length=120)),
                ('manager', models.CharField(max_length=120)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
