# Generated by Django 3.1.1 on 2020-10-07 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_personaldetail_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='account_password',
            field=models.TextField(null=True, unique=True),
        ),
    ]
