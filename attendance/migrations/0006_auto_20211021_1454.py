# Generated by Django 3.2.8 on 2021-10-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_employee_attendance_model_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_attendance_model',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='employee_attendance_model',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='employee_attendance_model',
            name='start_time',
        ),
        migrations.AddField(
            model_name='employee_attendance_model',
            name='end_date_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='employee_attendance_model',
            name='start_date_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
