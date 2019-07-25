# Core imports
from django.db import models

# Third party integration

# Apps imports


class Student(models.Model):
    identification_card = models.CharField(max_length=11, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"