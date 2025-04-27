from django.db import models
from django.utils import timezone

# Create your models here.
class Drinks(models.Model):
    drink=models.CharField(max_length=200)
    price=models.IntegerField
class MenuCategory(models.Model):
    menu_category_name=models.CharField(max_length=200)

class Menu(models.Model):
    name=models.CharField(max_length=200)
    description = models.TextField(default="No description available")
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Person(models.Model): 
    first_name = models.TextField(max_length=20) 
    last_name = models.TextField(max_length=20)
    def __str__(self): 
        return f"{self.last_name}, {self.first_name}" 


class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    guest_number = models.PositiveIntegerField()
    reservation_time = models.DateField(default=timezone.now)  # Cho phép nhập ngày
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_time}"





class Product(models.Model): 
    ProductID=models.IntegerField() 
    name= models.TextField() 
    category= models.TextField 
    class Meta: 
        permissions = [('can_change_category', 'Can change category')] 

 