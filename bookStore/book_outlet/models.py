from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=80)





class Address(models.Model):
    street = models.CharField(max_length= 100)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.street}, {self.postal_code}, {self.city}'

    class Meta:
        verbose_name_plural = 'Adress'


class Author(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return f"{self.name}"
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null= True)
    is_bestselling = models.BooleanField(default=False)
    publish_countires = models.ManyToManyField(Country)

    def __str__(self):
        return f"{self.title}, ({self.rating})"
