from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    miles = models.IntegerField()
    price = models.FloatField()
    address = models.TextField(max_length=255)
    pickup_address = models.TextField(max_length=255)
    drop_address = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_at = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.user} - {self.oid}"


class ContactUs(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    requirement = models.CharField(max_length=20)

class GetQuote(models.Model):
    fname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    message = models.TextField()
