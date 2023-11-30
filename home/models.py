from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    v_name = models.CharField(max_length=255)
    mandal = models.CharField(max_length=255)
    dist = models.CharField(max_length=255)
    sta = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
# models.py
from django.db import models
from django.contrib.auth.models import User

class food_req(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    city = models.CharField(max_length=100)
    mandal = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} order"
