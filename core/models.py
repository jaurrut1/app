from django.db import models

class Presupuesto(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class ItemPresupuesto(models.Model):
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE, related_name='items')
    nombre_item = models.CharField(max_length=255)
    unidad = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_item

class PrecioUnitario(models.Model):
    item = models.ForeignKey(ItemPresupuesto, on_delete=models.CASCADE, related_name='precios_unitarios')
    codigo_recurso = models.CharField(max_length=50)
    nombre_recurso = models.CharField(max_length=255)
    unidad = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_recurso
