# Generated by Django 3.2.5 on 2021-08-06 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileJson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_json', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
