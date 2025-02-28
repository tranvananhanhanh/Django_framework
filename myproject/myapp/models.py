from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink=models.CharField(max_length=200)
    price=models.IntegerField
class MenuCategory(models.Model):
    menu_category_name=models.CharField(max_length=200)
class Meu(models.Model):
    menu_item=models.CharField(max_length=200)
    price=models.IntegerField(null=False)
    category_id=models.ForeignKey(MenuCategory,on_delete=models.PROTECT,default=None,related_name="category_name")

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
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    guest_number = models.IntegerField(default=0)
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name+ '' +self.last_name


class Product(models.Model): 
    ProductID=models.IntegerField() 
    name= models.TextField() 
    category= models.TextField 
    class Meta: 
        permissions = [('can_change_category', 'Can change category')] 

 