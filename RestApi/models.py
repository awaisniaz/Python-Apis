from django.db import models
class UserRegitration(models.Model):
   # ID = models.AutoField(primary_key=True),
    Name = models.CharField(max_length=30),
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)
      
    confirmpassword=models.CharField(max_length=20)
    def __str__(self):
        return self.Name
