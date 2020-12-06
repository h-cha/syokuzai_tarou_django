from django.db import models

# Create your models here.

<<<<<<< HEAD
# Foodクラス
class Food(models.Model):
    foodName = models.CharField(max_length=20) #食材名

    def __str__(self):
        return self.foodName

# FoodSetクラス
class FoodSet(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    limitRegister = models.DateField(
        verbose_name='賞味・消費期限',
        blank=True,
        null=True,
    )
    foodGram = models.IntegerField(default=0)
=======
#Foodクラス
class Food(models.Model):
    foodName = models.CharField(max_length=20) #食材名

#FoodSetクラス
#class FoodSet(models.Model):
    #foodGram = models.IntegerField(max_length=10) #数量
>>>>>>> master
