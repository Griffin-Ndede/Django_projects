from django.db import models

# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.firstname} {self.age}"
