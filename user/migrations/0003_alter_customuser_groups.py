# Generated by Django 4.0 on 2022-01-10 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0002_remove_customuser_groups_customuser_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
