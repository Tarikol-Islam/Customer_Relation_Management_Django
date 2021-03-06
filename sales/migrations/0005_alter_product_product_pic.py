# Generated by Django 4.0 on 2022-01-18 04:59

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_remove_order_order_items_order_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_pic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1920, 1080], upload_to='Product/'),
        ),
    ]
