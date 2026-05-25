from django.db import models
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False, deleted_at=None)
    
    

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
        
        
    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
        
        
    def hard_delete(self):
        return super().get_queryset().delete()
    
    


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()
    
    
    class Meta:
        abstract = True