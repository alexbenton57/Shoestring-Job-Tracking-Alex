# Generated by Django 4.0.4 on 2022-05-24 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='op_name',
            new_name='name',
        ),
    ]