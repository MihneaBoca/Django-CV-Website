# Generated by Django 3.0.3 on 2020-07-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0006_auto_20200706_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='cv',
            name='phone_number',
            field=models.TextField(default=''),
        ),
    ]