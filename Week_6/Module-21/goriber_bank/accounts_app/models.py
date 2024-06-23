from django.db import models
#django amader ke built in user make korar facility day
from django.contrib.auth.models import User 
from .constants import ACCOUNT_TYPE, GENDER_TYPE

class userBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)#jehetu ekjon user er jonno 1 ta data takbe multipole username, name, email use korar sujuk nai ejonno
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)#account no dui jon user er same hobe na
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=15, decimal_places=5)#ekjon user 15 digit obdi taka rakthe parbe, and 5 dosomik ghor obdi rakthe parbe 100.34535

    def __str__(self):
        return str(self.account_no)

class userAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)    
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)    

    def __str__(self):
        return str(self.user.email)