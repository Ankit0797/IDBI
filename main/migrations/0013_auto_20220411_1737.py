# Generated by Django 3.2 on 2022-04-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_employees_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_permission',
            name='Employee_Department',
            field=models.CharField(choices=[('Finance', 'Finance'), ('PMO', 'PMO'), ('HR', 'HR')], default='Choose', max_length=100),
        ),
        migrations.AlterField(
            model_name='revoke_permission',
            name='Employee_Department',
            field=models.CharField(choices=[('Finance', 'Finance'), ('PMO', 'PMO'), ('HR', 'HR')], default='Choose', max_length=100),
        ),
    ]