from django.db import models
from math import ceil

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_clientes')

    def __str__(self):
        return f'{self.nome} {self.id}'

    class Meta:
        verbose_name_plural = 'Clientes'


class Veiculo(models.Model):
    fabricante = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=50)
    ano = models.CharField(max_length=10, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    placa = models.CharField(max_length=20)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_veiculos', blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.modelo} {self.placa}'

    class Meta:
        verbose_name_plural = 'Veículos'


class Parametro(models.Model):
    valor = models.DecimalField(max_digits=50, decimal_places=2)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.valor} - {self.descricao}'

    class Meta:
        verbose_name_plural = 'Parâmetros'


class Mensalista(models.Model):
    id_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    id_parametro = models.ForeignKey(Parametro, on_delete=models.CASCADE)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.id_veiculo} - {self.id_parametro}'

    class Meta:
        verbose_name_plural = 'Mensalistas'


class Rotativo(models.Model):
    data_entrada = models.DateTimeField(auto_now_add=None)
    data_saida = models.DateTimeField(auto_now_add=None, blank=True, null=True)
    id_parametro = models.ForeignKey(Parametro, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.data_entrada} ({self.id_veiculo})'

    class Meta:
        verbose_name_plural = 'Rotativos'

    def calculo_total(self):
        if self.data_saida:
            horas = ceil((self.data_saida - self.data_entrada).total_seconds() / 3600)
            obj = Parametro.objects.get(id=self.id_parametro.pk)
            self.total = horas * obj.valor
            return self.total
        return 0.0
