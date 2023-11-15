# presupuestos/admin.py

from django.contrib import admin
from .models import Presupuesto, ItemPresupuesto, PrecioUnitario

admin.site.register(Presupuesto)
admin.site.register(ItemPresupuesto)
admin.site.register(PrecioUnitario)
