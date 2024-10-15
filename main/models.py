from django.db import models

class RegisteredMember(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    panther_id = models.IntegerField(unique=True)
    degree = models.CharField(max_length=10)
    major = models.CharField(max_length=50)
    csc_1302 = models.BooleanField()
    
    # New field to store team numbers
    team_number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class WaitlistMember(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    panther_id = models.IntegerField(unique=True)
    degree = models.CharField(max_length=10)
    major = models.CharField(max_length=50)
    csc_1302 = models.BooleanField()  # New field to store CSC 1302 question

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

