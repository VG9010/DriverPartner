# Generated by Django 5.0.6 on 2024-09-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpvalid', '0013_alter_otptoken_otp_code_alter_ride_drop_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='892093', max_length=6),
        ),
    ]
