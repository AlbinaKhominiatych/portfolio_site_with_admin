# Generated by Django 4.2.2 on 2023-07-22 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='description',
            new_name='description_experience',
        ),
    ]
