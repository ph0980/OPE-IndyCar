from django import forms
from funilaria.models import Cliente,Empresa,Orcamento,OrdemDeServico,Customer,Material
import datetime
import localflavor.br.forms
from funilaria.views import *
from .widgets import FengyuanChenDatePickerInput

def somenteLetras(campo):
    if not campo:
        return False
    bloqueado = '0123456789!@#$%¨&*()_+`{}^:><|\,.;~]´[=-"'
    for i in bloqueado:
        if i in campo:
            return False
    return True

def somenteNumeros(campo):
    if not campo:
        return False
    try:
        campo=campo.replace(' ','')
        n=int(campo)
        return True
    except:
        return False

def validarTamanho(campo,tamanho):
    if not tamanho or not campo:
        return False
    return len(str(campo))==tamanho

def validarTelefone(tel):
    if not tel:
        return False
    return somenteNumeros(tel) and (len(str(tel)) in range(10,12))

def validarPlaca(placa):
    if not placa:
        return False
    bloqueado = '!@#$%¨&*()_+`{}^:><|\,.;~]´[=-" '
    for i in bloqueado:
        if i in placa:
            return False
    return True

def validarModelo(modelo):
    if not modelo:
        return False
    bloqueado = '!@#$%¨&*()_+`{}^:><|\,;~]´[=-"'
    for i in bloqueado:
        if i in modelo:
            return False
    return True

def validarAno(ano):
    if not ano:
        return False
    try:
        a = int(ano)
    except:
        return False
    now=datetime.datetime.now().year
    return a<=int(now)



class CustomerForm(forms.ModelForm):
    nome = forms.CharField(max_length=60,label='Nome completo:',widget = forms.TextInput(attrs={
        'placeholder':'informe o nome',
        'name':'nome',
        'id':'nome'}))
    endereco = forms.CharField(max_length=100,label='Endereço:',widget = forms.TextInput(attrs={
        'placeholder':'informe o endereço',
        'name':'endereco',
        'id':'endereco'}))
    bairro = forms.CharField(max_length=30,label='bairro:',widget = forms.TextInput(attrs={
        'placeholder':'informe o bairro',
        'name':'bairro',
        'id':'bairro'}))
    email = forms.EmailField(max_length=60,label='email:',widget = forms.EmailInput(attrs={
        'placeholder':'informe o email',
        'name':'email',
        'id':'email'}))
    telefone = forms.CharField(max_length=11,label='telefone:',widget = forms.TextInput(attrs={
        'placeholder':'informe o telefone',
        'name':'telefone',
        'id':'telefone'}))


    def validar(self):
        dados=self.cleaned_data
        nome=dados.get('nome')
        endereco=dados.get('endereco')
        bairro=dados.get('bairro')
        email=dados.get('email')
        telefone=dados.get('telefone')
        

        if not somenteLetras(nome):
            raise forms.ValidationError('Nome inválido !')

        if not somenteLetras(bairro):
            raise forms.ValidationError('Bairro inválido !')

        if not validarTelefone(telefone):
            raise forms.ValidationError('Telefone inválido !')

    class Meta:
        abstract=True



class ClienteForm(CustomerForm):
    cpf = localflavor.br.forms.CharField(max_length=12, min_length=12,label='cpf:',widget = forms.TextInput(attrs={
        'placeholder':'informe o cpf',
        'name':'cpf',
        'id':'cpf'}))

    def clean(self):
        return self.validar()

    class Meta:
        model = Cliente
        fields=['cpf','nome','endereco','bairro','email','telefone']

class EmpresaForm(CustomerForm):
    cnpj = localflavor.br.forms.CharField(min_length=14, max_length=14,label='cnpj:',widget = forms.TextInput(attrs={
        'placeholder':'informe o cnpj',
        'name':'cnpj',
        'id':'cnpj'}))

    def clean(self):
        dados = self.cleaned_data
        cnpj=dados.get('cnpj')
        if not somenteNumeros(cnpj) or not validarTamanho(cnpj,14):
            raise forms.ValidationError('CNPJ inválido !')
        self.validar()

    class Meta:
        model = Empresa
        fields=['cnpj','nome','endereco','bairro','email','telefone']

class OrcamentoForm(forms.ModelForm):
    quantidade_pecas = forms.IntegerField(label='quantidade_pecas:',widget = forms.TextInput(attrs={
        'placeholder':'informe a quantidade de peças',
        'name':'quantidade_pecas',
        'id':'quantidade_pecas'}))
    servicos = forms.CharField(max_length=500,label='servicos:',widget = forms.Textarea(attrs={
        'placeholder':'informe os serviços necessários',
        'name':'servicos',
        'id':'servicos'}))
    pecas = forms.CharField(max_length=200,label='Peças:',widget = forms.Textarea(attrs={
        'placeholder':'informe as Peças necessárias',
        'name':'Pecas',
        'id':'Pecas'}))
    
    valor_mao_de_obra = forms.FloatField(label='valor_mao_de_obra:',widget = forms.TextInput(attrs={
        'placeholder':'informe a mao_de_obra necessária',
        'name':'valor_mao_de_obra',
        'id':'valor_mao_de_obra'}))

    total_a_pagar = forms.DecimalField(label='total_a_pagar:',widget = forms.TextInput(attrs={
        'readonly':'total a pagar',
        'name':'total_a_pagar',
        'id':'total_a_pagar'}))
    
    previsao_entrega = forms.DateField(label='previsao_entrega:',widget = forms.DateInput(attrs={
        'placeholder':'informe a previsao entrega',
        'name':'previsao_entrega',
        'id':'previsao_entrega'}))
    data_saida = forms.DateField(label='data_saida:',widget = forms.DateInput(attrs={
        'placeholder':'informe a data de saida',
        'name':'data_saida',
        'id':'data_saida'}))
    
    def clean(self):
        dados=self.cleaned_data
        quantidade_pecas=dados.get('quantidade_pecas')
        servicos=dados.get('servicos')
        pecas=dados.get('pecas')
        valor_mao_de_obra=dados.get('valor_mao_de_obra')
        total_a_pagar=dados.get('total_a_pagar')
        previsao_entrega=dados.get('previsao_entrega')
        data_saida=dados.get('data_saida')

        if not somenteNumeros(quantidade_pecas):
            raise forms.ValidationError('quantidade_pecas inválida !')

        if not somenteLetras(servicos):
            raise forms.ValidationError('servicos inválido !')
        
        if not somenteLetras(pecas):
            raise forms.ValidationError('pecas inválida !')

        if not somenteNumeros(valor_mao_de_obra):
            raise forms.ValidationError('valor_mao_de_obra inválido !')

        if not somenteNumeros(total_a_pagar):
            raise forms.ValidationError('total_a_pagar inválido !')
        
    
    class Meta:
        model = Orcamento
        fields=['pecas','quantidade_pecas','servicos','valor_mao_de_obra','previsao_entrega','data_saida','total_a_pagar']

class OrdemDeServicoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Customer.objects.all().order_by('id'))
    marca = forms.CharField(max_length=10,label='marca:',widget = forms.TextInput(attrs={
        'placeholder':'informe a marca',
        'name':'marca',
        'id':'marca'}))
    modelo = forms.CharField(max_length=20,label='modelo:',widget = forms.TextInput(attrs={
        'placeholder':'informe o modelo',
        'name':'modelo',
        'id':'modelo'}))
    cor = forms.CharField(max_length=10,label='cor:',widget = forms.TextInput(attrs={
        'placeholder':'informe a cor',
        'name':'cor',
        'id':'cor'}))
    placa = forms.CharField(max_length=7,label='placa:',widget = forms.TextInput(attrs={
        'placeholder':'informe a placa',
        'name':'placa',
        'id':'placa'}))
    ano = forms.CharField(max_length=4,label='ano:',widget = forms.TextInput(attrs={
        'placeholder':'informe o ano',
        'name':'ano',
        'id':'ano'}))
    cidade = forms.CharField(max_length=10,label='cidade:',widget = forms.TextInput(attrs={
        'placeholder':'informe a cidade',
        'name':'cidade',
        'id':'cidade'}))
    ESTADO_CARRO= [
    ('AC', 'Acre'),    
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
    ('ET', 'Estrangeiro'),
    ]
    estado_veiculo= forms.CharField(label='Estado', widget=forms.Select(choices=ESTADO_CARRO))
    reparos_necessarios = forms.CharField(max_length=500,label='reparos_necessarios:',widget = forms.Textarea(attrs={
        'placeholder':'informe os reparos necessarios',
        'name':'reparos_necessarios',
        'id':'reparos_necessarios'}))
    prazo_entrega = forms.DateField(label='prazo_entrega:',input_formats=['%d/%m/%Y'],widget = FengyuanChenDatePickerInput(attrs={
        'placeholder':'informe o prazo de entrega',
        'name':'prazo_entrega',
        'id':'prazo_entrega'}))
    data_finalizacao = forms.DateField(required=False,label='data de finalização:',input_formats=['%d/%m/%Y'],widget = FengyuanChenDatePickerInput(attrs={
        'placeholder':'informe a data de finalização',
        'name':'data_finalizacao',
        'id':'data_finalizacao'}))
    
    def clean(self):
        dados=self.cleaned_data
        reparos_necessarios=dados.get('reparos_necessarios')
        entrada=dados.get('entrada')
        prazo_entrega=dados.get('prazo_entrega')
        finalizado=dados.get('finalizado')
        marca=dados.get('marca')
        modelo=dados.get('modelo')
        cor=dados.get('cor')
        placa=dados.get('placa')
        ano=dados.get('ano')
        cidade=dados.get('cidade')
        estado_veiculo=dados.get('estado_veiculo')

        if not somenteLetras(reparos_necessarios):
            raise forms.ValidationError('reparos necessarios inválida !')

        if not somenteLetras(marca):
            raise forms.ValidationError('Marca inválida !')

        if not validarModelo(modelo):
            raise forms.ValidationError('Modelo inválido !')

        if not somenteLetras(cor):
            raise forms.ValidationError('Cor inválida !')

        if not validarPlaca(placa):
            raise forms.ValidationError('Placa inválida !')

        if not validarAno(ano):
            raise forms.ValidationError('Ano inválido !')

        if not somenteLetras(cidade):
            raise forms.ValidationError('Cidade inválida !')

        if not somenteLetras(estado_veiculo):
            raise forms.ValidationError('Estado inválido !')

    class Meta:
        model = OrdemDeServico
        fields=['cliente','marca','modelo','cor','placa','ano','cidade','estado_veiculo','reparos_necessarios','prazo_entrega','data_finalizacao']



class MaterialForm(forms.ModelForm):
    quantidade_estoque = forms.IntegerField(label='quantidade_estoque:',widget = forms.TextInput(attrs={
        'placeholder':'informe a quantidade de estoque',
        'name':'quantidade_estoque',
        'id':'quantidade_estoque'}))
    descricao = forms.CharField(max_length=200,label='descricao:',widget = forms.Textarea(attrs={
        'placeholder':'informe a descrição',
        'name':'descricao',
        'id':'descricao'}))
    
    valor = forms.DecimalField(label='valor:',widget = forms.TextInput(attrs={
        'readonly':'valor da peça',
        'name':'valor',
        'id':'valor'}))
    
    def clean(self):
        dados=self.cleaned_data
        quantidade_estoque=dados.get('quantidade_estoque')
        descricao=dados.get('descricao')
        valor=dados.get('valor')
        
        if not somenteNumeros(quantidade_estoque):
            raise forms.ValidationError('quantidade inválida !')

        if not somenteLetras(descricao):
            raise forms.ValidationError('descricao inválido !')

        if not somenteNumeros(valor):
            raise forms.ValidationError('valor inválido !')
        
    
    class Meta:
        model = Material
        fields=['quantidade_estoque','descricao','valor']
