from django.db import models

# Create your models here.


class Module(models.Model):
    
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='modules/', null=True, blank=True)
    
    order = models.IntegerField(default=0)    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['order']
        db_table = 'module'
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'



class ModulePrice(models.Model):
    
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='prices')

    standart_price = models.IntegerField(default=0)
    standart_features = models.TextField()

    pro_price = models.IntegerField(default=0)
    pro_features = models.TextField()


    premium_price = models.IntegerField(default=0)
    premium_features = models.TextField()
    
    def __str__(self):
        return f"{self.module.name}"

    
    class Meta:
        db_table = 'module_price'
        verbose_name = 'Module Price'
        verbose_name_plural = 'Module Prices'
    