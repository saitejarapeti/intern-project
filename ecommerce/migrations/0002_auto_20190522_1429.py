# Generated by Django 2.2.1 on 2019-05-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]