# Generated by Django 3.0.7 on 2020-06-09 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BICAPweb', '0003_auto_20200609_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indagine',
            name='ultimaModifica',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='informazione',
            name='ultimaModifica',
            field=models.TimeField(auto_now=True),
        ),
    ]
