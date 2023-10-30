from django.db import models

class Producto(models.Model):
    precio = models.IntegerField()
    marca = models.CharField(max_length=50)

class Mancuerna(Producto):
    peso = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.peso} - {self.marca}'
    
class Maquina(Producto):
    nombre = models.CharField(max_length=100)
    peso_limite = models.IntegerField()
    instrucciones_de_uso = models.TextField(max_length=500)
    
    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.marca}'
    
class Barra(Producto):
    tipo_de_barra = (
        ('regular', 'Regular'),
        ('olimpica', 'Olimpica'),
    )
    
    tipo = models.CharField(choices=tipo_de_barra)
    peso = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.tipo} - {self.marca}'