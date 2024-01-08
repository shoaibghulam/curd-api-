from django.db import models
from django.contrib.auth.models import User
class About(models.Model):
    id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200 , default="Name")
    last_name = models.CharField(max_length=200 , default="Name")
    Dob= models.CharField(max_length=200 , default="Dob")
    Contact=models.CharField(max_length=200 , default="Contact")
    Address=models.CharField(max_length=200 , default="Address")
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first_name)