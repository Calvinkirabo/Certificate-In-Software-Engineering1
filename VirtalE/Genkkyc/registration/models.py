from django.db import models

# Create your models here.


class info (models.Model):
    f_name = models.CharField(max_length=120)
    l_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=150)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    z_code = models.CharField(max_length=100)
    number_1 = models.CharField(max_length=50)
    number_2 = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'