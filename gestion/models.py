from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patients(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=11)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - by ' + self.user.username


