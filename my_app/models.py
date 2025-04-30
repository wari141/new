from django.db import models

# Create your models here.
class customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, default='male')
    class Meta:
        db_table = 'customer'