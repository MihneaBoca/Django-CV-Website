# Generated by Django 3.0.3 on 2020-07-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0005_auto_20200706_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
