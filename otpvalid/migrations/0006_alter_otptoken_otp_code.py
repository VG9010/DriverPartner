# Generated by Django 5.0.6 on 2024-09-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpvalid', '0005_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='417fe6', max_length=6),
        ),
    ]
