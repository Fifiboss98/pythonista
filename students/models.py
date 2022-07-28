from django.db import models
from django.contrib.auth.models import User

class Student(User):
    centre = models.OneToOneField('Centre', on_delete=models.CASCADE)
    annee = models.OneToOneField('Annee', on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name

class Centre(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
        

class Annee(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Programme(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name