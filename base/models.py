from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class message(models.Model):
    body = models.CharField(max_length=10000)
    send = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send")
    receive = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receive")
    
    def __str__(self):
        return self.body
    