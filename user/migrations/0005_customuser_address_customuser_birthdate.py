# Generated by Django 4.0 on 2022-01-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_customuser_phone_alter_customuser_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='birthdate',
            field=models.DateTimeField(null=True),
        ),
    ]
