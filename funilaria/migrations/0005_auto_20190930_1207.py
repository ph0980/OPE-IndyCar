# Generated by Django 2.2 on 2019-09-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0004_auto_20190930_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='valor',
            field=models.FloatField(),
        ),
    ]