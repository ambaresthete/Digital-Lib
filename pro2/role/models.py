from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save

# Create your models here.

class Role(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rolename = models.CharField(max_length=120,default="student")

    def __str__(self):
        return self.rolename

def post_save_receiver(sender,instance,created,*args,**kwargs):
    if created:
        username=instance.username
        qs=User.objects.get(username=username)
        role=""
        if 'h' in username:
            role="student"
        else:
            role="staff"
        Role.objects.create(user=qs,rolename=role)


post_save.connect(post_save_receiver,sender=User)
