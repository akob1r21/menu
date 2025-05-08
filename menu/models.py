from django.db import models
from django.contrib.auth.models import User
class Foods(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
    

    class Meta:
        db_table = 'foods'
        managed = True
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Foods, on_delete=models.CASCADE, related_name='orders')
    phone_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_recieved = models.BooleanField(default=False)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'orders'
        managed = True
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    



