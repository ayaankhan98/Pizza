from django.db import models

# Create your models here.
class RegularPizza(models.Model):
    SINGLE = "S"
    MULTI = "M"
    TYPE = [
        (SINGLE,"Single"),
        (MULTI,"Multiple")
    ]
    item = models.CharField(max_length=64)
    type_of_dish = models.CharField(max_length=1, choices = TYPE)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f"{self.item} Small-{self.small} Large-{self.large} Type-{self.type_of_dish}"

class SilicianPizza(models.Model):
    SINGLE = "S"
    MULTI = "M"
    TYPE = [
        (SINGLE,"Single"),
        (MULTI,"Multiple")
    ]
    item = models.CharField(max_length=64)
    type_of_dish = models.CharField(max_length=1, choices = TYPE)
    small = models.FloatField()
    large = models.FloatField()
    
    def __str__(self):
        return f"{self.item} Small-{self.small} Large-{self.large}"


class Toppings(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"
    
class Subs(models.Model):
    item = models.CharField(max_length=64)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f"{self.item} Small-{self.small} Large-{self.large}"
class Extras(models.Model):
    item = models.CharField(max_length=64)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f"{self.item} Small-{self.small} Large-{self.large}"

class Pasta(models.Model):
    item = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.item} Price-{self.price}"

class Salads(models.Model):
    item = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.item} Price-{self.price}"
    
class DinnerPlatters(models.Model):
    item = models.CharField(max_length=64)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f"{self.item} Small-{self.small} Large-{self.large}"

class orders(models.Model):
    item = models.CharField(max_length=64)
    size = models.CharField(max_length=10,blank=True, null=True)
    quantity = models.IntegerField()
    user = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user} have {self.item} , quantity{self.quantity}, size - {self.size}"
