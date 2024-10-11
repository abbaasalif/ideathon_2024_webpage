from django.db import models

# Create your models here.
class RegisteredMember(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    panther_id = models.IntegerField(unique=True)
    degree = models.CharField(max_length=10)
    major = models.CharField(max_length=50)
    csc_1302 = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"