from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=64)
    bio = models.TextField(max_length=2000)
    fecha_publicacion = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.bio}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Producto(models.Model):
    nombre = models.CharField(max_length=256)
    precio = models.IntegerField()
    bio = models.TextField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.precio}"




