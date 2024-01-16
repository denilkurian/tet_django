from django.db import models
from django.contrib.auth.models import User



class Candidate(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    
   
   
class Trash(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)






