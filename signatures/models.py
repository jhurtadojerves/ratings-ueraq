# Core imports
from django.db import models

# Third party integration

# Locals apps import


class Signature(models.Model):
    name = models.CharField(max_length=128)
    hours_for_week = models.IntegerField()

    def __str__(self)
        return self.name

