# Generated by Django 3.1.1 on 2020-10-27 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20201027_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetail',
            name='account_password',
        ),
    ]