# Generated by Django 3.2.8 on 2021-10-21 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_common_response_alias_model_common_response_model_employee_attendance_model_longcodemodel_messagemod'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Common_Response_alias_Model',
        ),
        migrations.DeleteModel(
            name='Common_Response_Model',
        ),
        migrations.DeleteModel(
            name='LongcodeModel',
        ),
        migrations.DeleteModel(
            name='MessageModel',
        ),
        migrations.DeleteModel(
            name='Response_messages_Model',
        ),
    ]