# Generated by Django 2.2.2 on 2019-08-23 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0007_customer_veiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='veiculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='funilaria.Veiculo'),
        ),
    ]