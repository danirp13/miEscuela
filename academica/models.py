from django.db import models

# Create your models here.
class Materia(models.Model):
	"""docstring for Materia"""
	nombre=models.CharField(max_length=50,blank=True)

	def __str__(self):
		return self.nombre

class  Estudiante(models.Model):
	nombres=models.CharField(max_length=50,blank=True)
	apellido=models.CharField(max_length=50,blank=True)
	direccion=models.CharField(max_length=50,blank=True)
	email=models.EmailField(max_length=50)
	#photo=models.ImageField(upload_to='photo/')
	materia=models.ForeignKey(Materia)

	def __str__(self):
		return self.nombres+" "+self.apellido