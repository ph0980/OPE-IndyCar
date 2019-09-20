from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,HttpResponseRedirect
from funilaria.forms import ClienteForm,EmpresaForm,OrcamentoForm,OrdemDeServicoForm
from django.contrib import messages
from funilaria.models import Cliente,Customer,Empresa,Orcamento,OrdemDeServico
from django.contrib.auth.decorators import login_required
from datetime import date
# Create your views here.
#comentado pra n ficar obrigatorio
def pagina_inicial(request):
    return render(request, 'pagina-inicial.html')

@login_required(login_url='/login/')
def index (request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def cliente(request):
    clientes = Cliente.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'clientes.html',context={'clientes':clientes,'msg':msg})

@login_required(login_url='/login/')
def novocliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST or None)
        if form_cliente.is_valid():
            try:
                form_cliente.save()
                messages.success(request,'Cliente cadastrado com sucesso')
            except Exception as e:
                messages.error(request,e)
            return redirect(cliente)
        else:
            return render(request,'formulario_cliente.html',context={'form_cliente':form_cliente})
    else:
        form_cliente = ClienteForm()
        return render(request,'formulario_cliente.html',context={'form_cliente':form_cliente})

@login_required(login_url='/login/')
def editar_cliente(request,id=None):
    instance_cliente = get_object_or_404(Cliente,id=id)
    form_cliente = ClienteForm(request.POST or None, instance= instance_cliente)
    if form_cliente.is_valid():
        try:
            instance_cliente=form_cliente.save(commit=False)
            instance_cliente.save()
            messages.success(request,'Cliente atualizado com sucesso')
            return redirect(cliente)
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_cliente.html',context={'form_cliente':form_cliente,'instance_cliente':instance_cliente})

@login_required(login_url='/login/')
def deletar_cliente(request,id=None):
    instance = get_object_or_404(Cliente,id=id)
    try:
        instance.delete()
        messages.success(request,'Cliente deletado com sucesso')
    except Exception as e:
        messages.error(request,'Não foi possível deletar o cliente')
    return redirect(cliente)

@login_required(login_url='/login/')
def empresa(request):
    empresas = Empresa.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'empresas.html',context={'empresas':empresas,'msg':msg})

@login_required(login_url='/login/')
def novoempresa(request):
    if request.method == 'POST':
        form_empresa= EmpresaForm(request.POST or None)
        if form_empresa.is_valid():
            try:
                form_empresa.save()
                messages.success(request,'Empresa cadastrada com sucesso')
                return redirect(empresa)
            except Exception as e:
                messages.error(request,e)
        else:
            return render(request,'formulario_empresa.html',context={'form_empresa':form_empresa})
    else:
        form_empresa= EmpresaForm()
        return render(request,'formulario_empresa.html',context={'form_empresa':form_empresa})

@login_required(login_url='/login/')
def editar_empresa(request,id=None):
    instance = get_object_or_404(Empresa,id=id)
    form_empresa= EmpresaForm(request.POST or None, instance= instance)
    if form_empresa.is_valid():
        try:
            instance=form_empresa.save()
            instance.save()
            messages.success(request,'Empresa atualizada com sucesso')
            return redirect(empresa)
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_empresa.html',context={'form_empresa':form_empresa,'instance':instance})

@login_required(login_url='/login/')
def deletar_empresa(request,id=None):
    instance = get_object_or_404(Empresa,id=id)
    try:
        instance.delete()
        messages.success(request,'Empresa deletada com sucesso')
    except Exception as e:
        messages.error(request,'Não foi possível deletar a empresa')
    return redirect(empresa)


@login_required(login_url='/login/')
def novoorcamento (request):
    if request.method == 'POST':
        form_orcamento= OrcamentoForm(request.POST or None)
        if form_orcamento.is_valid():
            try:
                form_orcamento.save()
                messages.success(request,'Orcamento cadastrada com sucesso')
                return redirect(orcamento)
            except Exception as e:
                messages.error(request,e)
        else:
            return render(request,'formulario_orcamento.html',context={'form_orcamento':form_orcamento})
    else:
        form_orcamento= OrcamentoForm()
        return render(request,'formulario_orcamento.html',context={'form_orcamento':form_orcamento})


@login_required(login_url='/login/')
def ordem_de_servico(request):
    ordens = OrdemDeServico.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'os.html',context={'ordens':ordens,'msg':msg})

@login_required(login_url='/login/')
def nova_os(request):
    entrada=date.today()
    if request.method == 'POST':
        form_os= OrdemDeServicoForm(request.POST or None)
        if form_os.is_valid():
            try:
                form_os.save()
                messages.success(request,'Ordem de servico cadastrada com sucesso')
                return redirect(ordemdeservico)
            except Exception as e:
                messages.error(request,e)
        else:
            return render(request,'formulario_os.html',context={'form_os':form_os,'entrada':entrada})
    else:
        form_os= OrdemDeServicoForm()
        return render(request,'formulario_os.html',context={'form_os':form_os,'entrada':entrada})

def editar_orcamento():
    pass


def editar_os(request,id=None):
    instance = get_object_or_404(OrdemDeServico,id=id) 
    form_os= OrdemDeServicoForm(request.POST or None, instance=instance)
    cliente = form_os.instance.cliente
    print(type(cliente))
    entrada=instance.entrada if instance else None
    print(form_os.errors)
    if form_os.is_valid():
        try:
            instance=form_os.save()
            instance.save()
            messages.success(request,'OS atualizada com sucesso')
            return redirect(ordem_de_servico)
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_os.html',context={'form_os':form_os,'instance':instance,'cliente':cliente,'entrada':entrada})

def deletar_os(request):
    pass
