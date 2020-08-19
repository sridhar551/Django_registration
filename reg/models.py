from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=55, unique=True)
    password = models.CharField(max_length=16)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name + ' logged in successfully'