# Generated by Django 4.0 on 2022-01-19 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_support_status'),
        ('production', '0003_raworder_amount_raworder_amount_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raworder',
            name='order_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customuser'),
        ),
    ]