# Generated by Django 5.0.6 on 2024-06-25 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='emai',
            new_name='email',
        ),
    ]
