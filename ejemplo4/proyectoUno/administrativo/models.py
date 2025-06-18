from django.db import models

# Create your models here.
class Pais(models.Model):
    # nombre
    # capital
    # número de provincias
    # número de habitantes
    nombre = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    numero_de_provincias = models.IntegerField()
    numero_habitantes = models.IntegerField()

    def __str__(self):
        return "%s %s %d %d" % (self.nombre, self.capital, self.numero_de_provincias, self.numero_habitantes) 


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%s %s %s" % (self.nombre,
                self.apellido,
                self.cedula)

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)
