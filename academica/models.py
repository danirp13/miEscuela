from django.db import models

# Create your models here.
class  Estudiante(models.Model):
	nombres=models.CharField(max_length=50,blank=True)
	apellido=models.CharField(max_length=50,blank=True)
	direccion=models.CharField(max_length=50,blank=True)
	email=models.EmailField(max_length=50)
	#photo=models.ImageField(upload_to='photo/')
class Materia(models.Model):
	"""docstring for Materia"""
	nombre=models.CharField(max_length=50,blank=True)

