# Generated by Django 2.2 on 2019-09-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0005_auto_20190930_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
