# Generated by Django 2.2 on 2019-10-05 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=60)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2, unique=True)),
                ('nome', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=200)),
                ('quantidade_estoque', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='funilaria.Customer')),
                ('cpf', models.CharField(max_length=14, unique=True)),
            ],
            bases=('funilaria.customer',),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='funilaria.Customer')),
                ('cnpj', models.CharField(max_length=18, unique=True)),
            ],
            bases=('funilaria.customer',),
        ),
        migrations.CreateModel(
            name='OrdemDeServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_veiculo', models.CharField(max_length=30)),
                ('modelo_veiculo', models.CharField(max_length=30)),
                ('cor_veiculo', models.CharField(max_length=30)),
                ('ano_veiculo', models.SmallIntegerField()),
                ('placa_veiculo', models.CharField(max_length=8, unique=True)),
                ('cidade_veiculo', models.CharField(max_length=30)),
                ('reparos_necessarios', models.TextField(max_length=200)),
                ('entrada', models.DateField(auto_now_add=True)),
                ('prazo_entrega', models.DateField(blank=True, null=True)),
                ('data_finalizacao', models.DateField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funilaria.Customer')),
                ('estado_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funilaria.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicos', models.TextField(max_length=500)),
                ('valor_mao_de_obra', models.FloatField(blank=True, null=True)),
                ('previsao_entrega', models.DateField(blank=True, null=True)),
                ('data_saida', models.DateField(blank=True, null=True)),
                ('total_a_pagar', models.DecimalField(decimal_places=2, max_digits=8)),
                ('carrinho', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='funilaria.Carrinho')),
                ('ordem_servico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='funilaria.OrdemDeServico')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('selecionado', models.BooleanField(default=False)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funilaria.Material')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='carrinho',
            name='itens',
            field=models.ManyToManyField(to='funilaria.ItemCarrinho'),
        ),
        migrations.AddField(
            model_name='carrinho',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
