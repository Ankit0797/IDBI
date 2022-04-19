# Generated by Django 3.2 on 2022-04-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20220411_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_permission',
            name='Employee_Department',
            field=models.CharField(choices=[('Admin', 'Admin'), ('PMO', 'PMO'), ('HR', 'HR')], default='Choose', max_length=100),
        ),
        migrations.AlterField(
            model_name='revoke_permission',
            name='Employee_Department',
            field=models.CharField(choices=[('Admin', 'Admin'), ('PMO', 'PMO'), ('HR', 'HR')], default='Choose', max_length=100),
        ),
    ]