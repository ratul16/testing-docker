from django.db import models

# Create your models here.
class EmployeeInformationModel(models.Model):

    name = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    office = models.CharField(max_length = 200)
    age = models.IntegerField()
    salary = models.CharField(max_length = 200)