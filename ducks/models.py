from django.db import models


# Create your models here.
class Duck(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name