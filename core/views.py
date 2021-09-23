from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from core.forms import FormCliente, FormVeiculo, FormRotativo, FormParametro, FormMensalista
from core.models import Cliente, Veiculo, Rotativo, Parametro, Mensalista

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

@login_required
def cadastro_cliente(request):
    if request.user.is_staff:
        form = FormCliente(None or request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('url_listagem_clientes')
        contexto = {'form' : form,
                    'texto_title': 'CadCli',
                    'texto_titulo':'Cadastro Cliente',
                    'texto_botao':'Cadastrar',
                    'url_voltar':'url_principal'
                    }
        return  render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')


@login_required
def listagem_clientes(request):
    if request.user.is_staff:
        if request.POST and request.POST['cliente_input']:
            dados = Cliente.objects.filter(nome=request.POST['cliente_input'])
        else:
             dados = Cliente.objects.all()
        contexto = {'dados' : dados}
        return render(request, 'core/listagem_clientes.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')

class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

@login_required
def cadastro_veiculo(request):
    if request.user.is_staff:
        form = FormVeiculo(None or request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Veículo cadastrado com sucesso!")
            return redirect('url_listagem_veiculos')
        contexto = {
            'form': form,
            'texto_title': 'CadVeic',
            'texto_titulo': 'Cadastro Veiculo',
            'texto_botao': 'Cadastrar',
            'url_voltar': 'url_principal'
            }
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')

@login_required
def listagem_veiculos(request):
    if request.user.is_staff:
        if request.POST and request.POST['veiculo_input']:
            dados = Veiculo.objects.filter(modelo=request.POST['veiculo_input'])
        else:
            dados = Veiculo.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_veiculos.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')


def tabela(request):
    return render(request, 'core/tabela.html')

@login_required
def atualiza_cliente(request, id):

    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente atualizado com sucesso!")
            return  redirect('url_listagem_clientes')
        else:
            contexto = {
                'form':form,
                'texto_title': 'AtuCli',
                'texto_titulo':'Atualização Cliente',
                'texto_botao':'Atualizar',
                'url_voltar':'url_listagem_clientes'
            }
            return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')

@login_required
def atualiza_veiculo(request, id):

    if request.user.is_staff:
        obj = Veiculo.objects.get(id=id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Veículo atualizado com sucesso!")
            return redirect('url_listagem_veiculos')
        else:
            contexto = {
                'form':form,
                'texto_title': 'AtuVeic',
                'texto_titulo':'Atualização Veiculo',
                'texto_botao':'Atualizar',
                'url_voltar':'url_listagem_veiculos'
            }
            return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')

@login_required
def exclui_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        if request.POST:
            obj.delete()
            messages.success(request, "Cliente excluido com sucesso!")
            return redirect('url_listagem_clientes')
        else:
            contexto = {'dados': obj.nome, 'id': obj.id, 'url': 'url_listagem_clientes'}
            return render(request, 'core/confirma_exclusao.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')

def exclui_veiculo(request, id):
    if request.user.is_staff:
        obj = Veiculo.objects.get(id=id)
        if request.POST:
            obj.delete()
            messages.success(request, "Veículo excluído com sucesso!")
            return redirect('url_listagem_veiculos')
        else:
            contexto = {'dados': obj.placa, 'id': obj.id, 'url': 'url_listagem_veiculos'}
            return render(request, 'core/confirma_exclusao.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')


def listagem_rotativos(request):
    dados = Rotativo.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_rotativos.html', contexto)

def cadastro_rotativo(request):
    form = FormRotativo(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Rotativo cadastrado com sucesso!")
        return redirect('url_listagem_rotativos')
    contexto = {'form': form, 'texto_title': 'CadRot', 'texto_titulo': 'Cadastro de Rotativo',
                'texto_botao': 'Cadastrar', 'url_voltar':'url_principal'}
    return render(request, 'core/cadastro.html', contexto)


def atualiza_rotativo(request, id):
    obj = Rotativo.objects.get(id=id)
    form = FormRotativo(request.POST or None, instance=obj)
    if form.is_valid():
        obj.calculo_total()
        form.save()
        messages.success(request, "Rotativo atualizado com sucesso!")
        return redirect('url_listagem_rotativos')
    contexto = {'form': form, 'texto_title': 'AtuRot', 'texto_titulo': 'Atualiza Rotativo',
                'texto_botao': 'Atualizar', 'url_voltar': 'url_listagem_rotativos'}
    return render(request, 'core/cadastro.html', contexto)


def cadastro_mensalista(request):
    form = FormMensalista(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Mensalista cadastrado com sucesso!")
        return redirect('url_listagem_mensalistas')
    contexto = {'form': form, 'texto_title':'CadMensalista', 'texto_titulo':'Cadastro de Mensalista',
                'texto_botao':'Cadastrar', 'url_voltar':'url_principal'}
    return render(request, 'core/cadastro.html', contexto)


def listagem_mensalistas(request):
    dados = Mensalista.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_mensalistas.html', contexto)


def exclui_mensalista(request, id):
    if request.user.is_staff:
        obj = Mensalista.objects.get(id=id)
        if request.POST:
            obj.delete()
            messages.success(request, "Mensalista excluído com sucesso!")
            return redirect('url_listagem_mensalistas')
        else:
            contexto = {'dados': obj.id_veiculo, 'id': obj.id, 'url': 'url_listagem_mensalistas'}
            return render(request, 'core/confirma_exclusao.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')


def atualiza_mensalista(request, id):
    obj = Mensalista.objects.get(id=id)
    form = FormMensalista(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Mensalista atualizado com sucesso!")
        return redirect('url_listagem_mensalistas')
    contexto = {'form': form, 'texto_title': 'AtuMensa', 'texto_titulo': 'Atualiza Mensalista',
                'texto_botao': 'Atualizar', 'url_voltar': 'url_listagem_mensalistas'}
    return render(request, 'core/cadastro.html', contexto)



def exclui_rotativo(request, id):
    if request.user.is_staff:
        obj = Rotativo.objects.get(id=id)
        if request.POST:
            obj.delete()
            messages.success(request, "Rotativo excluído com sucesso!")
            return redirect('url_listagem_rotativos')
        else:
            contexto = {'dados': obj.id_veiculo, 'id': obj.id, 'url': 'url_listagem_rotativos'}
            return render(request, 'core/confirma_exclusao.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')


def cadastro_parametro(request):
    form = FormParametro(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Parâmetro cadastrado com sucesso!")
        return redirect('url_listagem_parametros')
    contexto = {'form': form, 'texto_title': 'CadTabela', 'texto_titulo': 'Cadastro de Tabela Preço',
                'texto_botao': 'Cadastrar', 'url_voltar':'url_principal'}
    return render(request, 'core/cadastro.html', contexto)


def listagem_parametros(request):
    dados = Parametro.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem_parametros.html', contexto)


def exclui_parametro(request, id):
    if request.user.is_staff:
        obj = Parametro.objects.get(id=id)
        if request.POST:
            obj.delete()
            messages.success(request, "Parâmetro excluído com sucesso!")
            return redirect('url_listagem_parametros')
        else:
            contexto = {'dados': obj.descricao, 'id': obj.id, 'url': 'url_listagem_parametros'}
            return render(request, 'core/confirma_exclusao.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')


def atualiza_parametro(request, id):
    obj = Parametro.objects.get(id=id)
    form = FormParametro(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Parâmetro atualizado com sucesso!")
        return redirect('url_listagem_parametros')
    contexto = {'form': form, 'texto_title': 'AtuPre', 'texto_titulo': 'Atualiza Preços',
                'texto_botao': 'Atualizar', 'url_voltar': 'url_listagem_parametros'}
    return render(request, 'core/cadastro.html', contexto)
