# Generated by Django 5.0.6 on 2024-09-12 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpvalid', '0010_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='649a69', max_length=6),
        ),
        migrations.AlterField(
            model_name='ride',
            name='drop_location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
