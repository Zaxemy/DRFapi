from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        
        
    def __str__(self):
        return self.name

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'Женщину'
        verbose_name_plural = 'Женщины'

    def __str__(self):
        return self.title