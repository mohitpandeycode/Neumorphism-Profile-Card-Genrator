# Generated by Django 4.2.7 on 2024-03-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_appuser_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='facebook',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='appuser',
            name='instagram',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='appuser',
            name='twitter',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='appuser',
            name='youtube',
            field=models.CharField(default='', max_length=500),
        ),
    ]
