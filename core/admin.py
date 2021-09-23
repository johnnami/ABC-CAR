from django.contrib import admin
from core.models import Cliente, Veiculo, Parametro, Rotativo, Mensalista

admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Parametro)
admin.site.register(Rotativo)
admin.site.register(Mensalista)

