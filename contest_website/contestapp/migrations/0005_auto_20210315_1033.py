# Generated by Django 3.1.4 on 2021-03-15 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestapp', '0004_auto_20210315_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_contest',
            name='date',
            field=models.CharField(default='YYYY-MM-DD', help_text='Date Format: <em>YYYY-MM-DD</em>.', max_length=200),
        ),
        migrations.AlterField(
            model_name='add_contest',
            name='time',
            field=models.CharField(default='18-00-00', help_text='Time Format: <em>24-00-00</em>.', max_length=200),
        ),
    ]
