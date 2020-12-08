from django.db import models
from accounts.models import CustomUser


# Create your models here.

# Foodクラス
class Food(models.Model):
    foodName = models.CharField(max_length=20) #食材名

#FoodSetクラス
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
    def __str__(self):
        return str(self.food)  + " [ " + str(self.limitRegister) + " ] " + str(self.foodGram)
    
    class Meta:
        ordering = ('-limitRegister',)

# Refrigeratorクラス
class Refrigerator(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    foodset = models.ForeignKey(FoodSet, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)  + " : "  + str(self.foodset)