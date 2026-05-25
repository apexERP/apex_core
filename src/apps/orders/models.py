from django.db import models

from core.softdelete import SoftDeleteModel
# Create your models here.


class Orders(SoftDeleteModel):


    class OrderStatus(models.TextChoices):
        NEW = 'new', 'New'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'

    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    order_status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.NEW)
    
    
    def __str__(self):
        return self.first_name
    
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'orders'
        
        
    