# Generated by Django 2.2.1 on 2019-05-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0019_item_additional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_1',
            field=models.ImageField(default='Basic', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='image_2',
            field=models.ImageField(default='Basic', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='image_3',
            field=models.ImageField(default='Basic', upload_to=''),
            preserve_default=False,
        ),
    ]