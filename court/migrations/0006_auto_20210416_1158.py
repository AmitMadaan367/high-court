# Generated by Django 2.2.1 on 2021-04-16 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0005_auto_20210415_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='copy',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lastorder',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
