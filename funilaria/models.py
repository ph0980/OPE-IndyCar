from django.db import models
from django.urls import reverse 
# Create your models here.

class Customer(models.Model):
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=8)
    email = models.EmailField(max_length=60)
    telefone = models.IntegerField(default=000000000)


class Cliente(Customer):
    rg = models.IntegerField()

    def get_editar_cliente(self):
        return reverse('editar_cliente',kwargs={'id':self.id})
    def get_del_cliente(self):
        return reverse('deletar_cliente',kwargs={'id':self.id})


class Empresa(Customer):
    cnpj = models.CharField(max_length=14)

    def get_editar_empresa(self):
        return reverse('editar_empresa',kwargs={'id':self.id})
    def get_del_empresa(self):
        return reverse('deletar_empresa',kwargs={'id':self.id})

class Veiculo(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=20)
    cor = models.CharField(max_length=10)
    ano = models.SmallIntegerField(default=0000)
    placa = models.CharField(max_length=7)
    cidade = models.CharField(max_length=10)
    estado = models.CharField(max_length=2)
    entrada = models.DateTimeField(auto_now_add=False, blank=False)
    finalizado = models.DateTimeField(auto_now_add=False, blank=False)

    def get_editar_veiculo(self):
        return reverse('editar_veiculo',kwargs={'id':self.id})
    def get_del_veiculo(self):
        return reverse('deletar_veiculo',kwargs={'id':self.id})


