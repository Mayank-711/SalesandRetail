from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    forgot_password_token=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class profile_photo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField(default='download.jpg',upload_to='profile_images',null=True)
    Name=models.CharField(max_length=50,null=True)

    def __str__(self):
        return f"{self.user.username}-profile_photo"