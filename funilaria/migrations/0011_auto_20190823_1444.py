# Generated by Django 2.2.2 on 2019-08-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0010_auto_20190823_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='entrada_veiculo',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='saida_veiculo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
