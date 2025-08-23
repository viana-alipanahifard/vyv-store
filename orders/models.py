from django.db import models
from django.contrib.auth import get_user_model
from home.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now

class Order(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='orders')
    paid=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    discount = models.IntegerField(blank=True, null=True, default=0)
    
    class Meta:
        ordering=('paid','-updated')
        
        
    def __str__(self):
        return f'{self.user} _ {str(self.id)}'
    
    def get_total_price(self):
        total = sum(item.get_cost() for item in self.order_item.all())  
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        return total




class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_item')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField(default=1)
    
    def __str__(self):
        return  f'{str(self.id)}'
         
    def get_cost(self):
        return (self.quantity)*(self.price)
         
        

class Coupon(models.Model):
	code = models.CharField(max_length=30, unique=True)
	valid_from = models.DateTimeField(default=now)
	valid_to = models.DateTimeField(default=now)
	discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(90)])
	active = models.BooleanField(default=False)

	def __str__(self):
		return self.code