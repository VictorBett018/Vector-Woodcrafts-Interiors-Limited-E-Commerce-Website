from django.db import models
from django.contrib.auth.models import User

   # Create your models here. 
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15, null= True)
    def _str_ (self):
        return self.user.email