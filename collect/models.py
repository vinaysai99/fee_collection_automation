from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    gender=[('Male','Male'),('Female','Female')]
    classType=[('B.Tech','B.Tech'),('M.Tech','M.Tech')]
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    phone = models.IntegerField(default=0)
    studentGender=models.CharField(max_length=20,choices=gender)
    date_birth=models.DateField(null=True)
    studentClass=models.CharField(max_length=20,choices=classType)
    Due=models.FloatField(default=0)
    def __str__(self):
        return self.user.username+" "+self.studentClass

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
