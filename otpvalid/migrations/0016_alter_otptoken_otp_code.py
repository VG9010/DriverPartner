# Generated by Django 5.0.6 on 2024-09-17 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpvalid', '0015_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='71a9df', max_length=6),
        ),
    ]
