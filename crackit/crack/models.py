from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=55, default='')
    email = models.EmailField(max_length=255)
    phone_no = models.CharField(max_length=10, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.name
