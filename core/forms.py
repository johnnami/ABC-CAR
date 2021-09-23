from django.forms import ModelForm
from core.models import Cliente, Veiculo, Rotativo, Parametro, Mensalista
from bootstrap_datepicker_plus import DateTimePickerInput


class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class FormVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class FormRotativo(ModelForm):
    class Meta:
        model = Rotativo
        fields = '__all__'
        widgets = {'data_entrada': DateTimePickerInput(), 'data_saida': DateTimePickerInput()}

class FormParametro(ModelForm):
    class Meta:
        model = Parametro
        fields = '__all__'


class FormMensalista(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'


