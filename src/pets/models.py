from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    @property
    def age(self):
        today = date.today()
        birth_date = self.dob.date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def __str__(self):
        return self.name