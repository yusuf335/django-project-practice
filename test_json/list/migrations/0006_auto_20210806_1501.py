# Generated by Django 3.2.5 on 2021-08-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_delete_choicemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
