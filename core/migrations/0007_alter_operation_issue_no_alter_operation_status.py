# Generated by Django 4.0.4 on 2022-05-26 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_operation_is_interim_alter_operation_phase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='issue_no',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Issue No.'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Complete', 'Complete'), (None, None)], default='Pending', editable=False, max_length=10, null=True, verbose_name='Op Status'),
        ),
    ]
