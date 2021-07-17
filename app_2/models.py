from django.db import models

# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name