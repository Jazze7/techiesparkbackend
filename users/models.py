from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=155)
    place=models.CharField(max_length=155)
    roll_no=models.IntegerField()
    email=models.EmailField(max_length=120)

    def __str__(self):
        return self.name
    

